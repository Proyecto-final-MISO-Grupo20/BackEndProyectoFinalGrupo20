
from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField, DecimalField
from tortoise.exceptions import ValidationError, DoesNotExist


class ContratoCandidato(Model):

    id = IntField(pk=True)
    fecha_inicio = DatetimeField(auto_now_add=True)
    fecha_fin = DatetimeField(auto_now_add=True)
    valor = IntField()
    ofertaId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
    
    


