from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class Usuario(Model):

    id = IntField(pk=True)
    nombre = CharField(max_length=150)
    tipoDocumento = IntField()
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
            user = await cls.filter(username=username)
            return user
        except DoesNotExist:
            return None


