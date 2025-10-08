import datetime
from bson import ObjectId

class Comentario:
    def __init__(self, id: ObjectId, postid: ObjectId, author: str, content: str, parentCommentId: ObjectId = None):
        self._id = id if id else ObjectId()
        self.postId = postid  if postid else ObjectId()
        self.author = author
        self.content = content
        self.parentCommentId = parentCommentId
        self.created_at = datetime.utcnow()

    def to_dict(self):
        """Converte o objeto Comentario para um dicionário para ser salvo no MongoDB."""
        return {
            "_id": self._id,
            "postId": self.postId,
            "author": self.author,
            "content": self.content,
            "createdAt": self.created_at,
            "parentCommentId": self.parentCommentId
        }