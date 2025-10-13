from typing import Optional
from pymongo.database import Database
from .base import BaseRepository
from domain import Usuario

class UserRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "users", Usuario)

    # Métodos específicos para Usuario
    def find_by_email(self, email: str) -> Optional[Usuario]:
        """Busca um usuário pelo seu endereço de e-mail."""
        document = self.collection.find_one({"email": email})
        if document:
            return Usuario(**document)
        return None

    def find_by_username(self, username: str) -> Optional[Usuario]:
        """Busca um usuário pelo seu nome de usuário."""
        document = self.collection.find_one({"username": username})
        if document:
            return Usuario(**document)
        return None