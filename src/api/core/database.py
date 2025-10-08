from pymongo import MongoClient
from .config import settings 

# Usa os valores do objeto 'settings' para conectar ao banco
client = MongoClient(settings.MONGO_CONNECTION_STRING)
db = client[settings.MONGO_DB_NAME]

print(f"Conectado ao banco de dados: {settings.MONGO_DB_NAME}")