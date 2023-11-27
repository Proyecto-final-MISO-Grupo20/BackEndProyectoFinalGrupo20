from tortoise.models import Model
from tortoise.fields import IntField, CharField
from tortoise.exceptions import ValidationError

from src.enums import EstadoOferta


class Oferta(Model):
    id = IntField(pk=True)
    perfil = CharField(max_length=255)
    proyecto_id = IntField()
    estado = CharField(max_length=20)

    async def save(self, *args, **kwargs):

        if not EstadoOferta.has_value(self.estado):
            raise ValidationError('Invalid state value, it must be DISPONIBLE, ASIGNADO, EVALUANDO, CONTRATADO, '
                                  'or FINALIZADO')

        await super().save(*args, **kwargs)

    @classmethod
    async def list(cls, estado_oferta: str):
        ofertas: list = []

        if estado_oferta is None:
            ofertas = await cls.all()

        if estado_oferta is not None:
            ofertas = await cls.filter(estado=estado_oferta)

        return ofertas

    @classmethod
    async def list_by_project_id(cls, project_id: int):
        offers: list = []

        if project_id is not None:
            offers = await cls.filter(proyecto_id=project_id)

        return offers
