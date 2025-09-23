import datetime
from bson import ObjectId

class Usuario:
    def __init__(self, username, email, password_hash, name, terms_accepted,
                 avatar_url=None, instituicao=None, profile_data=None, 
                 _id=None, created_at=None, updated_at=None):
        self._id = _id if _id else ObjectId()
        self.username = username
        self.email = email
        self.password = password_hash 
        self.name = name
        self.avatarUrl = avatar_url
        self.instituicao = instituicao if instituicao else {}
        self.termsAccepted = terms_accepted
        self.profileData = profile_data if profile_data else {}
        self.createAt = created_at if created_at else datetime.utcnow()
        self.updateAt = updated_at if updated_at else datetime.utcnow()
    
    def to_dict(self):
        """Converte o objeto Usuario para um dicionário para ser salvo no MongoDB."""
        return {
                "_id": self._id,
                "username": self.username,
                "email": self.email,
                "password": self.password,
                "name": self.name,
                "avatarUrl": self.avatarUrl,
                "instituicao": self.instituicao,
                "termsAccepted": self.termsAccepted,
                "profileData": self.profileData,
                "createAt": self.createAt,
                "updateAt": self.updateAt
            }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Cria uma instância de Usuario a partir de um dicionário vindo do MongoDB."""
        return cls(
            _id=data.get("_id"),
            username=data.get("username"),
            email=data.get("email"),
            password_hash=data.get("password"),
            name=data.get("name"),
            avatar_url=data.get("avatarUrl"), # ou avatar_url se você renomear
            instituicao=data.get("instituicao"),
            terms_accepted=data.get("termsAccepted"),
            profile_data=data.get("profileData"),
            created_at=data.get("createAt"),
            updated_at=data.get("updateAt")
        )