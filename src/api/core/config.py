import os
from dotenv import load_dotenv

# Carrega as variáveis do ambiente do arquivo .env
# Certifique-se de que o arquivo .env está no diretório raiz do projeto.
load_dotenv()

class Settings:
    """
    Classe que centraliza e carrega todas as configurações da aplicação,
    lendo-as a partir das variáveis de ambiente.
    """
    # --- Configurações do Banco de Dados (MongoDB) ---
    # Caso as variáveis de ambiente não estejam definidas, usa valores padrão.
    MONGO_CONNECTION_STRING: str = os.getenv("MONGO_CONNECTION_STRING", "mongodb://localhost:27017/")
    MONGO_DB_NAME: str = os.getenv("MONGO_DB_NAME", "default_db")

    # --- Configurações de Segurança (JWT) ---
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "uma_chave_secreta_padrao_e_nao_segura")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    # --- Configurações da Aplicação ---
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "False").lower() in ('true', '1', 't')
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", 8000))

    # --- Informações da Aplicação ---
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    AUTH_VERSION: str = os.getenv("AUTH_VERSION", "1.0.0")
    PORTAL_NAME: str = os.getenv("PORTAL_NAME", "DefaultPortal")

# Passo 2: Cria uma única instância da classe.
settings = Settings()