from tortoise.models import Model
from tortoise.fields import IntField, CharField, DatetimeField
from tortoise.exceptions import ValidationError



class Entrevista(Model):

    id = IntField(pk=True)
    titulo = CharField(max_length=125)
    fecha = DatetimeField(auto_now_add=True)
    calificacion  = IntField()
    comentario = CharField(max_length=255)

    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)

