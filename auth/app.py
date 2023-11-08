from flask import Flask, jsonify

from helpers.extensions import register_blueprints, initialize_database, setup_jwt
from flask_jwt_extended import JWTManager

app: Flask = Flask(__name__)

with app.app_context():
    setup_jwt(app)
    jwt = JWTManager(app)


    @jwt.invalid_token_loader
    def invalid_token_loader(callback):
        return jsonify({'error': 'Token inválido'}), 401


    initialize_database(app)
    register_blueprints(app)
