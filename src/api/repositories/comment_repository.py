from typing import List
from pymongo.database import Database
from .base import BaseRepository
from domain import Comentario

class CommentRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "comments", Comentario)

    # Métodos específicos para Comentario
    def find_by_post_id(self, post_id: str, skip: int = 0, limit: int = 100) -> List[Comentario]:
        """Busca todos os comentários de uma postagem específica."""
        cursor = self.collection.find({"postId": post_id}).skip(skip).limit(limit)
        return [Comentario(**doc) for doc in cursor]