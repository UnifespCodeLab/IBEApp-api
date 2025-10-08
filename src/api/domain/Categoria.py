from bson import ObjectId

class Categoria:
    def __init__(self, id: ObjectId, name: str):
        self._id = id if id else ObjectId()
        self.name = name

    def to_dict(self):
        return {
            "_id": str(self._id),
            "name": self.name
        }