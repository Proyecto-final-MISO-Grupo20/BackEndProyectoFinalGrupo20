import dataclasses
from dataclasses import dataclass


@dataclass
class GetGradesDto:

    grade: str
    comment: str

    @classmethod
    def get_attributes(cls):
        return [key.name for key in dataclasses.fields(GetGradesDto)]
