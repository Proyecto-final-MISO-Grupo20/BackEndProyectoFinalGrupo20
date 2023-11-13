from dataclasses import dataclass
from http import HTTPStatus


@dataclass
class PruebaDto:
    nombre: str
    tipo: int
    calificacion: int
    comentario: str 
