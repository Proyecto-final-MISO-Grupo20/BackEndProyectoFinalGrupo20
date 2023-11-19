from datetime import timedelta

import unittest
from flask import Flask
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash

from config import JWT_SECRET_KEY
from controllers.auth_controller import auth
from models import Usuario
from database import db


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///:memory'
        self.jwt = JWTManager(self.app)
        self.app.config["JWT_SECRET_KEY"] = 'MySecretKey'
        self.app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
        db.init_app(self.app)

        self.app.register_blueprint(auth)

        self.client = self.app.test_client()

        with self.app.app_context():

            db.create_all()

            # Create a test user
            password_hash = generate_password_hash('test_password')

            user = Usuario(nombre='Cesar Rivera',
                           tipo_documento=1,
                           documento='232233333',
                           username='test_user',
                           email='test@example.com',
                           password=password_hash,
                           rol=1)
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login_success(self):
        response = self.client.post("/auth/login", json={"username": "test_user", "password": "test_password"})
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn("token", data)

    def test_login_invalid_credentials(self):
        response = self.client.post('/auth/login', json={'username': 'test_user', 'password': 'wrong_password'})
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Email or password are incorrect')

    def test_login_without_all_fields(self):
        response = self.client.post("/auth/login", json={"username": "test_user"})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", data)

    def test_whoami_authenticated(self):
        login_response = self.client.post("/auth/login", json={"username": "test_user", "password": "test_password"})
        token = login_response.get_json()['token']
        headers = {"Authorization": f"Bearer {token}"}

        response = self.client.get("/auth/me", headers=headers)
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['username'], 'test_user')

    def test_whoami_unauthenticated(self):
        response = self.client.get('/auth/me')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['Error'], 'El token no es válido o está vencido.')
        # self.assertIsNone(data)

    def test_validate_health(self):
        response = self.client.get("/auth/ping")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"pong")


if __name__ == "__main__":
    unittest.main()
