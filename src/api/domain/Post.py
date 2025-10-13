from typing import List
from pydantic import Field
from .Base import MongoModel, PyObjectId

class Postagem(MongoModel):
    author_id: PyObjectId = Field(..., alias="authorId")
    category_id: PyObjectId = Field(..., alias="categoryId")
    title: str = Field(..., max_length=200)
    content: str
    tags: List[str] = Field(default_factory=list)
    is_featured: bool = Field(default=False, alias="isFeatured")