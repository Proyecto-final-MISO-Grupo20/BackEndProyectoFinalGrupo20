import dataclasses
from dataclasses import dataclass
from .skills_data_dto import SkillsDataDto


@dataclass
class GetOfferDto:
    perfil: str
    skills: list[SkillsDataDto]

    @classmethod
    def get_attributes(cls):
        return [key.name for key in dataclasses.fields(GetOfferDto)]
