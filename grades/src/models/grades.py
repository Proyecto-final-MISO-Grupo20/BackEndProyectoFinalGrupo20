from tortoise.models import Model
from tortoise.fields import IntField, CharField


class Grades(Model):

    id = IntField(pk=True)
    grade = IntField(null=False)
    comment = CharField(max_length=255)
    candidate_id = IntField()
    project_id = IntField()

    class Meta:
        unique_together = [("candidate_id", "project_id")]

    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
