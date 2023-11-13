
from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


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
    async def findByUserId(cls, user_id):
        candidatos = await cls.filter(usuarioId=user_id)
        
        if candidatos:
            return candidatos[0]  # Devuelve el primer candidato de la lista
        else:
            return None  # No se encontraron candidatos
        
    @classmethod
    async def get_by_id(cls, candidato_id):
        try:
            candidato = await Candidato.get(id=candidato_id)
            return candidato
        except DoesNotExist:
            return None
    


