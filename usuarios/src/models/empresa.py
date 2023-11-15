
from tortoise.models import Model
from tortoise.fields import IntField


class Empresa(Model):

    id = IntField(pk=True)
    tipoEmpresaID = IntField() 
    segmentoID = IntField()
    usuarioId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)

    @classmethod
    async def find_by_user_id(cls, user_id):
        empresa = await cls.filter(usuarioId=user_id)

        if empresa:
            return empresa[0]
        else:
            return None

