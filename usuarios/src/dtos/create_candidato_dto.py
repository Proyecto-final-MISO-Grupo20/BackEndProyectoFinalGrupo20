import dataclasses
from datetime import date
from dataclasses import dataclass

@dataclass
class CreateCandidatoDto:

    nombre: str
    tipo_documento: int
    documento: str
    username: str
    password: str
    email: str
    fecha_nacimiento: date
    telefono: int
    pais: str
    ciudad: str

    def get_attributes(self):
        return[key.name for key in dataclasses.fields(CreateCandidatoDto)]
