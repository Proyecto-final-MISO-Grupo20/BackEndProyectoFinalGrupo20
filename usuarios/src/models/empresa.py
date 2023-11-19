from tortoise.exceptions import DoesNotExist
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
        try:
            empresa = await cls.get(usuarioId=user_id)
            return empresa
        except DoesNotExist:
            return None

