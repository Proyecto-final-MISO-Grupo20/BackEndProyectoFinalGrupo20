from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class Empleado(Model):

    id = IntField(pk=True)
    nombre = CharField(max_length=255)
    tipo_documento = IntField()
    documento = CharField(max_length=25)
    cargo = CharField(max_length=100)
    email = CharField(max_length=255)
    empresaId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
    
    @classmethod
    async def findByEmpresaId(cls, id):
        empleados: list = []
        empleados = await cls.filter(empresaId=id)
        
        if empleados:
            return empleados 
        else:
            return None  # No se encontraron registros

