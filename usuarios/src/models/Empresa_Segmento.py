from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class Segmento(Model):

    empresaId = IntField()
    segmentoId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
    


