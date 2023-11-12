from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class Usuario(Model):

    id = IntField(pk=True)
    nombre = CharField(max_length=150)
    tipo_documento = IntField()
    documento = CharField(max_length=25)
    username = CharField(max_length=25)
    password = CharField(max_length=255)
    email = CharField(max_length=255)
    rol = IntField()
    
    @classmethod
    def find_by_id(cls, user_id: int):
        return cls.filter(id=user_id).first()
