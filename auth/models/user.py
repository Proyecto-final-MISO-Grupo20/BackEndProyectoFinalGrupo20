from sqlalchemy import Sequence

from models.base_model import BaseModel
from database import db

USER_ID_SEQ = Sequence('user_id_seq')


class User(BaseModel):
    id = db.Column(db.Integer, USER_ID_SEQ, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
