import dataclasses
from dataclasses import dataclass


@dataclass
class GetSkillDto:
    nombre: str
    tipo: str

    def get_attributes():
        return [key.name for key in dataclasses.fields(GetSkillDto)]
