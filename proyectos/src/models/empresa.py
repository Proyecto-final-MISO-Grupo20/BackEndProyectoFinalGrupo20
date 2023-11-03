
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
    async def findByUserId(cls, user_id):
        empresas = await cls.filter(usuarioId=user_id)
        
        if empresas:
            return empresas[0]  # Devuelve el primer empresas de la lista
        else:
            return None  # No se encontraron empresas

