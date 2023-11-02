import dataclasses
from datetime import date
from dataclasses import dataclass

@dataclass
class CreateEmpleadoDto:

    nombre: str
    tipo_documento: int
    documento: str
    cargo: str
    email: str

    def get_attributes(self):
        return[key.name for key in dataclasses.fields(CreateEmpleadoDto)]
