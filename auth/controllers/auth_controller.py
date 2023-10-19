from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token
from werkzeug.security import check_password_hash

from models.usuario import Usuario
from models.login_dto import LoginDto
from services.user_service import get_auth_by_id

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    data_keys = [key for key in data]
    login_keys = LoginDto.get_attributes(None)
    print('entro aca 0.')
    if not all(key in data_keys for key in login_keys):
        print('entro aca 1.')
        return jsonify({'error': 'La petición no contiene todos los campos requeridos.'}), 400
    print('entro aca 2.')
    user = Usuario.find_by_username(data['username'])
    
    if user and check_password_hash(user.password, data['password']):
        token = create_access_token(identity=user.id)

        return jsonify(token=token)

    return jsonify({'error': 'Email or password are incorrect'}), 404


@auth.route('/me', methods=['GET'])
@jwt_required(optional=True)
def whoami():
    user_id = get_jwt_identity()
    user = get_auth_by_id(user_id)

    return user


@auth.route('/ping', methods=['GET'])
def validate_health():
    return 'pong'
