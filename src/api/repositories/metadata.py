import datetime
from bson import ObjectId

def create_metadata(userId: ObjectId) ->dict:
    """
    Retorna um dicionário com os campos de metadados para um novo documento.
    """
    now = datetime.datetime.now(datetime.timezone.utc)
    return {
        "metadata": {
            "created_at": now,
            "created_by": userId,
            "uptadet_at": now,
            "updated_by": userId,
            "version": 1
        }
    }

def update_metadata(userId: ObjectId) -> dict:
    """
    Retorna um dicionário para ser usado com o operador $set do MongoDB
    para atualizar os metadados de um documento.
    """
    return {
          "$set": {
                "metadata.updated_at": datetime.datetime.now(datetime.timezone.utc),
                "metadata.updated_by": userId
          },
        "$inc": {"metadata.version": 1}
    }