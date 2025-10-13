from typing import Optional
from pydantic import Field
from .Base import MongoModel, PyObjectId

class Comentario(MongoModel):
    post_id: PyObjectId = Field(..., alias="postId")
    author_id: PyObjectId = Field(..., alias="authorId")
    content: str
    parent_comment_id: Optional[PyObjectId] = Field(None, alias="parentCommentId")