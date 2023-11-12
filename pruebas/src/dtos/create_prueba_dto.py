import dataclasses
from dataclasses import dataclass


@dataclass
class CreatePruebaDto:
    postulacionId: int
    calificacion: int
    comentario: str
    tipo: int
    nombre: str

    def get_attributes(cls):
        return[key.name for key in dataclasses.fields(CreatePruebaDto)]