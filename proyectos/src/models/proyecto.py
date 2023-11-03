from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class Proyecto(Model):

    id = IntField(pk=True)
    nombre = CharField(max_length=150)
    descripcion = CharField(max_length=250)
    codigo = IntField()
    empresaId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
    
    

