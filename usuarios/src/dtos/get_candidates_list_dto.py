from datetime import date
from dataclasses import dataclass


@dataclass
class GetCandidatesListDto:
    id: int
    usuarioId: int
    fecha_nacimiento: date
    telefono: int
    pais: str
    ciudad: str
