import dataclasses
from datetime import date
from dataclasses import dataclass

@dataclass
class CreateProyectoDto:

    nombre: str
    descripcion: str
    codigo: int

    def get_attributes(self):
        return[key.name for key in dataclasses.fields(CreateProyectoDto)]
