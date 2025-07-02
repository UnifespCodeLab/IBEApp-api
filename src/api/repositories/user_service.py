from typing import Optional, List
from ..repositories.base import UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_user_by_id(self, user_id: str) -> Optional[dict]:
        """Busca um usuário. A metadata já vem populada pelo repositório."""
        # Se for necessário um tratamento de erro ou lógica de permissão, ela entraria aqui.
        return self.user_repo.find_by_id(user_id)

    def get_all_users(self) -> List[dict]:
        """Busca todos os usuários."""
        return self.user_repo.find_all()
    
    def create_user(self, name: str, email: str, creator_id: str) -> dict:
        """
        Cria um novo usuário, passando o ID do criador para a auditoria.
        
        :param name: Nome do novo usuário.
        :param email: Email do novo usuário.
        :param creator_id: ID do usuário autenticado que está realizando a ação.
        """
        
        user_data = {"name": name, "email": email}
        
        return self.user_repo.save(user_data, current_user_id=creator_id)

    def update_user(self, user_id_to_update: str, update_data: dict, updater_id: str) -> Optional[dict]:
        """
        Atualiza um usuário existente, passando o ID do atualizador para a auditoria.
        
        :param user_id_to_update: ID do usuário a ser atualizado.
        :param update_data: Dicionário com os campos a serem atualizados.
        :param updater_id: ID do usuário autenticado que está realizando a ação.
        """
        update_data['id'] = user_id_to_update
        
        return self.user_repo.save(update_data, current_user_id=updater_id)