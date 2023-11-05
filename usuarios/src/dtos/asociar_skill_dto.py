import dataclasses
from datetime import date
from dataclasses import dataclass

@dataclass
class AsociarSkillDto:

    skill: int
    nivel_dominio: int


    def get_attributes(self):
        return[key.name for key in dataclasses.fields(AsociarSkillDto)]
