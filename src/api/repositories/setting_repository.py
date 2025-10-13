from typing import Optional
from pymongo.database import Database
from .base_repository import BaseRepository
from domain import Setting

class SettingRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "settings", Setting)

    def get_settings(self) -> Optional[Setting]:
        """
        Recupera o único documento de configurações.
        Se não existir, pode criar um com valores padrão.
        """
        document = self.collection.find_one()
        if document:
            return Setting(**document)
        else:
            # Opcional: Criar configurações padrão na primeira vez que for acessado
            default_settings = Setting()
            return self.create(default_settings)

    def update_settings(self, data: dict) -> Optional[Setting]:
        """Atualiza o documento de configurações."""
        # Tenta encontrar um documento para atualizar, se não, cria um 
        result = self.collection.update_one(
            {},  # Filtro vazio para corresponder a qualquer documento
            {"$set": data, "$currentDate": {"updateAt": True}},
            upsert=True
        )
        return self.get_settings()