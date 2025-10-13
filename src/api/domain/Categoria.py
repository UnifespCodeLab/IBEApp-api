from typing import Optional
from pydantic import Field
from .Base import MongoModel

class Categoria(MongoModel):
    name: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=500)