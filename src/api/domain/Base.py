from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict, BeforeValidator
from typing_extensions import Annotated

# --- Helper de Validação para ObjectId ---
# Esta é a configuração reutilizável para garantir que o Pydantic entenda o ObjectId do MongoDB.
PyObjectId = Annotated[
    ObjectId,
    BeforeValidator(lambda v: ObjectId(v) if isinstance(v, str) else v)
]

# --- Modelo Base Reutilizável ---
# Define configurações e campos comuns para todos os modelos que interagem com o MongoDB.
class MongoModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow, alias="createAt")
    updated_at: datetime = Field(default_factory=datetime.utcnow, alias="updateAt")

    # Configurações do Pydantic v2
    model_config = ConfigDict(
        populate_by_name=True,      # Permite criar a partir de dict com aliases (ex: "_id")
        arbitrary_types_allowed=True, # Permite tipos como ObjectId
        json_encoders={ObjectId: str} # Define como ObjectId é convertido para JSON
    )