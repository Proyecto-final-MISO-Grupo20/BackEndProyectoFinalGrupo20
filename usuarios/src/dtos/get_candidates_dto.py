from datetime import date
from dataclasses import dataclass

from src.dtos import SkillsDataResponseDto


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

    
