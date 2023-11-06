from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class Proyecto_Empleado(Model):

    id = IntField(pk=True)
    proyectoId = IntField()
    empleadoId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)

    @classmethod
    async def findByProjectEmployed(cls, projectId, employedId):
        empleado = await cls.filter(proyectoId=projectId, empleadoId=employedId)
        
        if empleado:
            return empleado[0]  # Devuelve el primer empresas de la lista
        else:
            return None  # No se encontraron registros
    
    

