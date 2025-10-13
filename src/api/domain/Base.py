from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict, BeforeValidator
from typing_extensions import Annotated
from enum import Enum

PyObjectId = Annotated[
    ObjectId,
    BeforeValidator(lambda v: ObjectId(v) if isinstance(v, str) else v)
]

# Define configurações e campos comuns para todos os modelos que interagem com o MongoDB.
class MongoModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow, alias="createAt")
    updated_at: datetime = Field(default_factory=datetime.utcnow, alias="updateAt")

    model_config = ConfigDict(
        populate_by_name=True,      # Permite criar a partir de dict com aliases (ex: "_id")
        arbitrary_types_allowed=True, # Permite tipos como ObjectId
        json_encoders={ObjectId: str} # Define como ObjectId é convertido para JSON
    )

class UserRole(str, Enum):
    USER = "user"
    SPECIALIST = "specialist"
    ADMIN = "admin"