
from tortoise.models import Model
from tortoise.fields import IntField


class Empresa(Model):

    id = IntField(pk=True)
    tipoEmpresaID = IntField() 
    segmentoID = IntField()
    usuarioId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)

