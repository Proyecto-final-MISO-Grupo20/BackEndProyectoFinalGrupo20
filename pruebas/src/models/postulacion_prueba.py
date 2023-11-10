from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class Postulacion_Prueba(Model):

    id = IntField(pk=True)
    postulacionId = IntField()
    pruebaId = IntField()
    calificacion = IntField()
    comentario = CharField(max_length=255)
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
