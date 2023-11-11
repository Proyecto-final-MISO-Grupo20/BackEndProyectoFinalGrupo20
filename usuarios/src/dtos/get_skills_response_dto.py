from dataclasses import dataclass
from .skill_dto import SkillDto


@dataclass
class GetSkillsResponseDto:
    skills: list[SkillDto]
