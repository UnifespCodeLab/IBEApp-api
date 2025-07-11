from typing import Protocol, Optional, List, Dict

class UserRepository(Protocol):
    """
    Define o contrato (a interface) para todas as operações de acesso
    a dados relacionadas à entidade 'Usuário'.

    Qualquer classe de repositório de usuário 
    DEVE implementar todos estes métodos para ser considerada compatível.
    """

    def find_by_id(self, user_id: str) -> Optional[Dict]:
        """
        Busca um único usuário pelo seu ID. Retorna o documento ou None se não encontrado.
        """
        ...

    def find_all(self,
                 active_only: bool = True,
                 email: Optional[List[str]] = None,
                 username: Optional[List[str]] = None) -> List[Dict]:
        """
        Busca uma lista de usuários, com a possibilidade de aplicar filtros.
        Retorna uma lista de documentos, que pode ser vazia.
        """
        ...

    def save(self, user_data: Dict, current_user_id: str) -> Dict:
        """
        Salva (cria ou atualiza) um documento de usuário no banco.
        Requer o ID do usuário realizando a ação para fins de auditoria (metadata).
        Retorna o documento salvo, como ele está no banco após a operação.
        """
        ...

    def delete(self, user_id: str) -> None:
        """
        Deleta um usuário pelo seu ID. Não retorna nada.
        """
        ...