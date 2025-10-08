from pymongo.collection import Collection
from bson import ObjectId
from typing import Optional, List
from pymongo import ReturnDocument

from metadata import update_metadata, create_metadata
from .base import UserRepository

class UserRepository:
    """
    Esta é a IMPLEMENTAÇÃO CONCRETA do contrato UserRepository, específica para o MongoDB.
    """
    def __init__(self, collection: Collection):
        self.collection = collection

    def find_by_id(self, user_id: str) -> Optional[dict]:
        """Busca um usuário pelo seu ID."""
        document = self.collection.find_one({"_id": ObjectId(user_id)})
        if document and "_id" in document:
            document["id"] = str(document["_id"])
            del document["_id"]
        return document

    def find_all(self) -> List[dict]:
        """Busca todos os usuários."""
        cursor = self.collection.find({}).sort("_id", 1)
        results = []
        for doc in cursor:
            if "_id" in doc:
                doc["id"] = str(doc["_id"])
                del doc["_id"]
            results.append(doc)
        return results

    def save(self, user_data: dict, current_user_id: str) -> dict:
        """
        Salva um usuário (cria se não existir, ou atualiza se existir).
        A operação é atômica e retorna o documento final como ele está no banco.

        :param user_data: Dicionário com os dados do usuário a serem salvos.
        :param current_user_id: O ID do usuário que está realizando a operação.
        """
        actor_user_id = ObjectId(current_user_id)

        # --- CASO DE CRIAÇÃO ---
        if "id" not in user_data:
            metadata_fields = create_metadata(actor_user_id)
            user_data.update(metadata_fields)
            
            result = self.collection.insert_one(user_data)
            
            user_data["id"] = str(result.inserted_id)
            if "_id" in user_data: del user_data["_id"] 
            
            return user_data

        # --- CASO DE ATUALIZAÇÃO ---
        else:
            user_id_str = user_data.pop("id") 

            update_payload = {
                "$set": user_data,
                **update_metadata(actor_user_id) 
            }
            
            updated_document = self.collection.find_one_and_update(
                {"_id": ObjectId(user_id_str)},
                update_payload,
                return_document=ReturnDocument.AFTER 
            )
            
            if updated_document:
                updated_document["id"] = str(updated_document["_id"])
                del updated_document["_id"]

            return updated_document

    def delete(self,user_id: str):
        """Deleta um usuario pelo seu ID"""
        result = self.collection.delete_one({"_id": ObjectId(user_id)})

        if result.deleted_count == 0:
            # Lançar um erro ou um aviso que o usuário não foi encontrado
            print(f"Aviso: Nenhum documento deletado para o ID {user_id}.")