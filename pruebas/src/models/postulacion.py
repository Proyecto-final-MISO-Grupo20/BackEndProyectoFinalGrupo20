from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class Postulacion(Model):

    id = IntField(pk=True)
    candidatoId = IntField()
    ofertaId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
    
    @classmethod
    async def getPostulacion(cls, candidato, oferta):
        try:
            print(candidato)
            print(oferta)
            postulacion = await cls.filter(candidatoId=candidato, ofertaId=oferta)
            print(postulacion)
            if postulacion:
                return postulacion[0]
            else:
                return None
        except DoesNotExist:
            return None

