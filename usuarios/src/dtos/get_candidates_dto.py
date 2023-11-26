from datetime import date
from dataclasses import dataclass

from .skills_data_response_dto import SkillsDataResponseDto
from .get_grades_response_dto import GetGradesResponseDto


@dataclass
class GetCandidatesDto:
    id: int
    usuario_id: int
    fecha_nacimiento: date
    telefono: int
    pais: str
    ciudad: str
    nombre: str
    tipo_documento: int
    documento: str
    email: str
    skills: [SkillsDataResponseDto]
    grades: [GetGradesResponseDto]
