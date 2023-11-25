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

    @classmethod
    async def find_by_candidate_id(cls, candidate_id):
        candidate_grades: list = []

        if candidate_id is not None:
            candidate_grades = await cls.filter(candidate_id=candidate_id)

        return candidate_grades
