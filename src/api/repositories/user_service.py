from typing import Dict, Optional
from bson import ObjectId
from domain.User import Usuario
from .user_repository import UserRepository  # Sua implementação concreta do repositório
from .utils import hash_password, verify_password, create_token_pair # Utilitários de segurança

class UserService:
    """
    Serviço focado em casos de uso de autenticação e gerenciamento de perfil de usuário.
    """
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, dto: Dict) -> Usuario:
        """
        Registra um novo usuário no sistema.
        :param dto: Dicionário com dados como 'username', 'email', 'password', 'name'.
        """
        if not all(k in dto for k in ['username', 'email', 'password']):
            raise ValueError("Campos 'username', 'email' e 'password' são obrigatórios.")

        if self.user_repository.find_by_email(dto['email']):
            raise ValueError(f"O email '{dto['email']}' já está em uso.")

        hashed_pwd = hash_password(dto['password'])

        new_user = Usuario(
            username=dto['username'],
            email=dto['email'],
            password_hash=hashed_pwd,
            name=dto.get('name', ''), 
            terms_accepted=dto.get('terms_accepted', False)
        )
        
        # 5. Persistir no banco através do repositório
        return self.user_repository.save(new_user)

    def login(self, creds: Dict) -> Dict:
        """
        Autentica um usuário e retorna um par de tokens.
        :param creds: Dicionário com 'email' e 'password'.
        """
        if not all(k in creds for k in ['email', 'password']):
            raise ValueError("Campos 'email' e 'password' são obrigatórios.")

        user = self.user_repository.find_by_email(creds['email'])
        if not user:
            raise ValueError("Credenciais inválidas.") 

        if not verify_password(creds['password'], user.password):
            raise ValueError("Credenciais inválidas.")

        token_pair = create_token_pair(user_id=str(user._id), username=user.username)

        return token_pair

    def update_profile(self, user_id: ObjectId, dto: Dict) -> Usuario:
        """
        Atualiza dados do perfil de um usuário.
        :param user_id: ID do usuário a ser atualizado.
        :param dto: Dicionário com os campos a serem alterados (ex: 'name', 'avatar_url').
        """
        # 1. Buscar o usuário que será atualizado
        user_to_update = self.user_repository.find_by_id(user_id)
        if not user_to_update:
            raise ValueError(f"Usuário com ID '{user_id}' não encontrado.")

        # 2. Atualizar os atributos do objeto com os dados do DTO
        # REGRA DE NEGÓCIO: Impedir a alteração de campos sensíveis por este método
        for key, value in dto.items():
            if hasattr(user_to_update, key) and key not in ['_id', 'email', 'username', 'password']:
                setattr(user_to_update, key, value)
        
        # 3. Salvar as alterações
        return self.user_repository.save(user_to_update)