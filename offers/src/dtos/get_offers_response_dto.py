from dataclasses import dataclass


@dataclass
class GetOffersResponseDto:
    id: int
    perfil: str
    proyecto_id: int
    estado: str
    contratado_id: str
