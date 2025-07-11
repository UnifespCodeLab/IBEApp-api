import bcrypt

def hash_password(plain_password: str) -> str:
    """
    Gera o hash de uma senha em texto puro usando bcrypt.
    O sal é gerado e embutido no hash final.
    """
    # 1. Converte a senha de string para bytes (necessário para o bcrypt)
    password_bytes = plain_password.encode('utf-8')
    
    # 2. Gera um sal aleatório
    salt = bcrypt.gensalt()
    
    # 3. Gera o hash da senha com o sal
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    
    # 4. Converte o hash de bytes para string para ser armazenado no banco
    return hashed_bytes.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica se uma senha em texto puro corresponde a um hash existente.
    """
    # 1. Converte ambas as senhas para bytes
    plain_password_bytes = plain_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    
    # 2. O bcrypt.checkpw extrai o sal do `hashed_password` automaticamente
    #    e compara os hashes de forma segura.
    return bcrypt.checkpw(plain_password_bytes, hashed_password_bytes)