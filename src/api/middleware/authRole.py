from functools import wraps
from flask import request, jsonify, g, current_app
import jwt
from src.api.domain.Base import UserRole 

def role_required(allowed_roles: list[UserRole]):
    """
    Decorator que aceita uma lista de Roles permitidas.
    Ex uso: @role_required([UserRole.ADMIN, UserRole.SPECIALIST])
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = None
            
            # 1. Extração do Token (Igual ao anterior)
            if 'Authorization' in request.headers:
                try:
                    token = request.headers['Authorization'].split(" ")[1]
                except IndexError:
                    return jsonify({'message': 'Token mal formatado'}), 401
            
            if not token:
                return jsonify({'message': 'Token ausente'}), 401

            try:
                # 2. Decodificar e Buscar Usuário
                data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
                # Assumindo que você usa current_app.db para acessar o PyMongo
                user = current_app.db.users.find_one({'_id': data['sub']}) # ou converter str p/ ObjectId se necessario

                if not user:
                    return jsonify({'message': 'Usuário inválido'}), 401
                
                # 3. VERIFICAÇÃO COM ENUM
                # Convertemos a string do banco para o Enum para garantir comparação segura
                # Se o user['role'] no banco for "admin", user_role será UserRole.ADMIN
                try:
                    user_role_enum = UserRole(user.get('role'))
                except ValueError:
                    # Se tiver algo no banco que não bate com o Enum
                    return jsonify({'message': 'Role do usuário inválida'}), 403

                # Verificamos se a role do usuário está na lista de permitidos
                if user_role_enum not in allowed_roles:
                    return jsonify({'message': 'Acesso negado'}), 403
                
                g.user = user # Salva para uso na rota

            except Exception as e:
                return jsonify({'message': 'Erro de autenticação', 'details': str(e)}), 401

            return f(*args, **kwargs)
        return decorated_function
    return decorator