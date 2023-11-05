import dataclasses
from dataclasses import dataclass


@dataclass
class GetSkillDto:
    nombre: str
    tipo: str

    @classmethod
    def get_attributes(cls):
        return [key.name for key in dataclasses.fields(GetSkillDto)]
