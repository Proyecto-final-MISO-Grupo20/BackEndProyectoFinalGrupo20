import dataclasses
from datetime import date
from dataclasses import dataclass

@dataclass
class CreateCandidatoDto:

    nombre: str
    tipoDocumento: int
    documento: str
    username: str
    password: str
    email: str
    fechaNacimiento: date
    telefono: int
    pais: str
    ciudad: str

    def get_attributes(self):
        return[key.name for key in dataclasses.fields(CreateCandidatoDto)]
