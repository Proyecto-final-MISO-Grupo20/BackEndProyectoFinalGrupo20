from sqlalchemy import Sequence
from models.base_model import BaseModel
from database import db

USER_ID_SEQ = Sequence('user_id_seq')


class Usuario(BaseModel):
    id = db.Column(db.Integer, USER_ID_SEQ, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, unique=False, nullable=False)
    tipo_documento = db.Column(db.Integer, unique=False, nullable=False)
    documento = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, nombre: str, tipo_documento: int, documento: str, username: str, email: str, password: str, rol: int):
        self.nombre = nombre
        self.tipo_documento = tipo_documento
        self.documento = documento
        self.username = username
        self.email = email
        self.password = password
        self.rol = rol
