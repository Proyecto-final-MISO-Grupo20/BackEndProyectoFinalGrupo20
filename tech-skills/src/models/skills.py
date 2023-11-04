from tortoise.models import Model
from tortoise.fields import IntField, CharField
from tortoise.exceptions import ValidationError

from src.enums import TipoSkill


class Skills(Model):

    id = IntField(pk=True)
    nombre = CharField(max_length=255)
    tipo = CharField(max_length=20)

    async def save(self, *args, **kwargs):

        if not TipoSkill.has_value(self.tipo):
            raise ValidationError('Invalid skill type, it must be HERRAMIENTA, HABILIDAD or IDIOMA')

        await super().save(*args, **kwargs)

    @classmethod
    async def list(cls, tipo_skill: str):
        skills_list: list = []

        if tipo_skill is None:
            skills_list = await cls.all()

        if tipo_skill is not None:
            skills_list = await cls.filter(tipo=tipo_skill)

        return skills_list
