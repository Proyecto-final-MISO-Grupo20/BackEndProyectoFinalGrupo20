from dataclasses import dataclass
from .prueba_dto import PruebaDto


@dataclass
class PostulacionDto:
    id: int
    nombre: str
    email: str
    telefono: int
    pruebas: list[PruebaDto]
