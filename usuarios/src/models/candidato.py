from tortoise.models import Model
from tortoise.fields import IntField, CharField, DatetimeField


class Candidato(Model):

    id = IntField(pk=True)
    fecha_nacimiento = DatetimeField(auto_now_add=True)
    telefono = IntField()
    pais = CharField(max_length=25)
    ciudad = CharField(max_length=30)
    usuarioId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
    
    @classmethod
    async def find_by_user_id(cls, user_id):
        candidatos = await cls.filter(usuarioId=user_id)
        
        if candidatos:
            return candidatos[0]
        else:
            return None

    @classmethod
    async def list(cls):
        candidates_list = await cls.all()

        return candidates_list
