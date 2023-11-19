from tortoise.models import Model
from tortoise.fields import IntField, CharField
from tortoise.exceptions import DoesNotExist

from src.dtos import GetUserDto


class Usuario(Model):

    id = IntField(pk=True)
    nombre = CharField(max_length=150)
    tipo_documento = IntField()
    documento = CharField(max_length=25)
    username = CharField(max_length=25)
    password = CharField(max_length=255)
    email = CharField(max_length=255)
    rol = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
    
    @classmethod
    async def get_by_username(cls, username):
        try:
            user = await cls.get(username=username)
            return user
        except DoesNotExist:
            return None

    @classmethod
    async def get_by_id(cls, user_id):
        try:
            user = await cls.get(id=user_id)
            user_data = GetUserDto(user.id, user.nombre, user.tipo_documento, user.documento, user.email)
            return user_data
        except DoesNotExist:
            return None


