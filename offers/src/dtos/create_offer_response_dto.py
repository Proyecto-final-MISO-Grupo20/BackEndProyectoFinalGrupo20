from dataclasses import dataclass
from .skills_data_response_dto import SkillsDataResponseDto


@dataclass
class CreateOfferResponseDto:
    id: int
    perfil: str
    proyecto_id: str
    estado: str
    skills: list[SkillsDataResponseDto]
