from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class Prueba(Model):

    id = IntField(pk=True)
    nombre = CharField(max_length=255)
    tipo = IntField()

    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
    
    @classmethod
    def find_by_id(cls, prueba_id: int):
        return cls.filter(id=prueba_id).first()