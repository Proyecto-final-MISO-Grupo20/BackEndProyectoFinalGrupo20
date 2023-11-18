from tortoise.models import Model
from tortoise.fields import IntField


class EntrevistaUsuario(Model):
    id = IntField(pk=True)
    entrevistaId = IntField()
    usuarioId = IntField()

    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)

    @classmethod
    async def listByUser(cls, usuario: int):
        entrevistas: list = []

        
        entrevistas = await cls.filter(usuarioId=usuario)
        return entrevistas