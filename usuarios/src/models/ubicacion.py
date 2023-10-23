
from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError


class Ubicacion(Model):

    id = IntField(pk=True)
    direccion = CharField(max_length=255)
    pais = CharField(max_length=30)
    ciudad = CharField(max_length=30)
    empresaId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)

