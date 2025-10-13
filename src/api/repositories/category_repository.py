from typing import Optional
from pymongo.database import Database
from .base import BaseRepository
from domain import Categoria

class CategoryRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "categories", Categoria)

    def find_by_name(self, name: str) -> Optional[Categoria]:
        """Busca uma categoria pelo nome."""
        document = self.collection.find_one({"name": name})
        if document:
            return Categoria(**document)
        return None