
from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError


class Candidato(Model):

    id = IntField(pk=True)
    fechaNacimiento = DatetimeField(auto_now_add=True)
    telefono = IntField()
    pais = CharField(max_length=25)
    ciudad = CharField(max_length=30)
    usuarioId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)

