from flask import Blueprint, request, jsonify, current_app
from pydantic import ValidationError
from src.api.schema.auth import LoginSchema
from src.api.core.security import verify_password, create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    raw_data = request.get_json()
    
    try:
        login_data = LoginSchema(**raw_data)
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

    # 3. Buscar usuário no MongoDB
    # current_app.db é a conexão injetada (PyMongo)
    user = current_app.db.users.find_one({"email": login_data.email})

    # 4. Verificar Credenciais
    # Use a mesma mensagem de erro para "User not found" 
    # e "Wrong password" para evitar enumeração de usuários.
    if not user or not verify_password(login_data.password, user.get('password')):
        return jsonify({"message": "Email ou senha incorretos"}), 401

    # 5. Gerar Token JWT
    # Convertemos o ObjectId para string
    token = create_access_token(user_id=str(user['_id']), role=user['role'])

    # 6. Retornar Sucesso
    return jsonify({
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": str(user['_id']),
            "username": user['username'],
            "role": user['role']
        }
    }), 200