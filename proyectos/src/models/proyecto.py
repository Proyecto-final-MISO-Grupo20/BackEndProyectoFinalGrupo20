from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class Proyecto(Model):

    id = IntField(pk=True)
    nombre = CharField(max_length=150)
    descripcion = CharField(max_length=250)
    codigo = IntField()
    empresaId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
    
    @classmethod
    async def findByEmpresaId(cls, id):
        proyectos: list = []
        proyectos = await cls.filter(empresaId=id)
        
        if proyectos:
            return proyectos 
        else:
            return None  # No se encontraron registros

    @classmethod
    async def find_by_id(cls, project_id):
        try:
            project = await cls.get(id=project_id)
            return project
        except DoesNotExist:
            return None
