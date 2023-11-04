import dataclasses
from dataclasses import dataclass


@dataclass
class CreateSkillDto:
    skills: list

    def get_attributes(self):
        return [key.name for key in dataclasses.fields(CreateSkillDto)]
