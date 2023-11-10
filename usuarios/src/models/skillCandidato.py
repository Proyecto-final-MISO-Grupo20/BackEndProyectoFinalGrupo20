from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class SkillCandidato(Model):

    id = IntField(pk=True)
    candidatoId = IntField()
    skillId = IntField()
    nivel_dominio = IntField()

    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)

    @classmethod
    async def list(cls, candidato_id: int):
        skills_list: list = []

        if candidato_id is not None:
            skills_list = await cls.filter(candidatoId=candidato_id)

        return skills_list
