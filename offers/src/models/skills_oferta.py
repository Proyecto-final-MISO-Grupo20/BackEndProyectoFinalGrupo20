from tortoise.models import Model
from tortoise.fields import IntField


class SkillsOferta(Model):
    id = IntField(pk=True)
    oferta_id = IntField()
    skill_id = IntField()
    dominio = IntField()

    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
