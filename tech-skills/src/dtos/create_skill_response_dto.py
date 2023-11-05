from dataclasses import dataclass


@dataclass
class CreateSkillResponseDto:
    id: int
    nombre: str
    tipo: str
