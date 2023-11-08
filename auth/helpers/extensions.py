from datetime import timedelta
from flask import Flask

from controllers.auth_controller import auth
from config import DATABASE_URL, JWT_SECRET_KEY
from database import db


def initialize_database(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

    db.init_app(app)


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(auth)


def setup_jwt(app: Flask) -> None:
    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=5)
