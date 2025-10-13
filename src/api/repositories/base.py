from typing import List, Optional, Type, TypeVar
from bson import ObjectId
from pymongo.database import Database
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class BaseRepository:
    def __init__(self, db: Database, collection_name: str, model: Type[T]):
        self.db = db
        self.collection = self.db[collection_name]
        self.model = model

    def create(self, data: T) -> T:
        """Cria um novo documento no banco de dados."""
        document = data.model_dump(by_alias=True, exclude_none=True)
        result = self.collection.insert_one(document)
        document['_id'] = result.inserted_id
        return self.model(**document)

    def find_by_id(self, item_id: str) -> Optional[T]:
        """Busca um documento pelo seu ID."""
        document = self.collection.find_one({"_id": ObjectId(item_id)})
        if document:
            return self.model(**document)
        return None

    def find_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        """Busca todos os documentos com paginação."""
        cursor = self.collection.find().skip(skip).limit(limit)
        return [self.model(**doc) for doc in cursor]

    def update(self, item_id: str, data: dict) -> Optional[T]:
        """Atualiza um documento existente."""
        result = self.collection.update_one(
            {"_id": ObjectId(item_id)},
            {"$set": data, "$currentDate": {"updateAt": True}}
        )
        if result.modified_count:
            return self.find_by_id(item_id)
        return None

    def delete(self, item_id: str) -> bool:
        """Deleta um documento pelo seu ID."""
        result = self.collection.delete_one({"_id": ObjectId(item_id)})
        return result.deleted_count > 0