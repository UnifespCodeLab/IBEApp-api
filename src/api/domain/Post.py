import datetime
from bson import ObjectId

class Post:
    def __init__(self, title: str, content: str, categoryId: ObjectId, tags: list = None, _id: ObjectId = None):
        self._id = _id if _id else ObjectId()
        self.categoryId = categoryId
        self.title = title
        self.content = content
        
        # Atribui a lista de tags. Se nenhuma for passada, cria uma lista vazia.
        self.tags = tags if tags is not None else []
        
        # Define as datas de criação e atualização uma única vez
        now = datetime.datetime.now(datetime.timezone.utc) # Método recomendado para UTC
        self.createdAt = now
        self.updatedAt = now

    def to_dict(self):
        """Converte o objeto Post para um dicionário para ser salvo no MongoDB."""
        return {
            "_id": self._id,
            "categoryId": self.categoryId,
            "title": self.title,
            "content": self.content,
            "tags": self.tags, 
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }