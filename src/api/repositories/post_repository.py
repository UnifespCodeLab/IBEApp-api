from typing import List
from pymongo.database import Database
from .base import BaseRepository
from domain import Postagem

class PostRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "posts", Postagem)

    # Métodos específicos para Postagem
    def find_by_author(self, author_id: str, skip: int = 0, limit: int = 100) -> List[Postagem]:
        """Busca todas as postagens de um autor específico."""
        cursor = self.collection.find({"authorId": author_id}).skip(skip).limit(limit)
        return [Postagem(**doc) for doc in cursor]

    def find_by_category(self, category_id: str, skip: int = 0, limit: int = 100) -> List[Postagem]:
        """Busca todas as postagens de uma categoria específica."""
        cursor = self.collection.find({"categoryId": category_id}).skip(skip).limit(limit)
        return [Postagem(**doc) for doc in cursor]