from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class Herramientas(Model):

    id = IntField(pk=True)
    herramienta = CharField(max_length=255)
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
    


