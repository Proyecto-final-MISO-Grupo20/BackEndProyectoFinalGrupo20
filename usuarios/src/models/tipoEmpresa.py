from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class TipoEmpresa(Model):

    id = IntField(pk=True)
    tipo = CharField(max_length=255)
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
    


