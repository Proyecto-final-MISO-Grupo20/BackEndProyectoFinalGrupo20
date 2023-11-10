from dataclasses import dataclass
from .skill_dto import SkillDto

@dataclass
class SkillsDataResponseDto:
    id: int
    dominio: int
    skill: SkillDto
