import bcrypt
import jwt
import datetime
from flask import current_app

def hash_password(plain_password: str) -> str:
    """Gera o hash de uma senha em texto puro usando bcrypt."""
    password_bytes = plain_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    return hashed_bytes.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se uma senha em texto puro corresponde a um hash existente."""
    if not plain_password or not hashed_password:
        return False
    
    plain_password_bytes = plain_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    
    # Retorna True se bater, False se falhar
    return bcrypt.checkpw(plain_password_bytes, hashed_password_bytes)

def create_access_token(user_id: str, role: str) -> str:
    """
    Cria um Token JWT contendo o ID do usuário e sua Role.
    Expira em 24 horas (ajuste conforme necessário).
    """
    payload = {
        "sub": user_id,       # Subject (Quem é o dono do token)
        "role": role,         # Permissão (Para facilitar checagem no front)
        "iat": datetime.datetime.utcnow(), # Issued At (Criado em)
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24) # Expiração
    }
    
    return jwt.encode(
        payload, 
        current_app.config['SECRET_KEY'], 
        algorithm="HS256"
    )