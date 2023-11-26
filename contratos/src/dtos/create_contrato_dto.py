import dataclasses
from dataclasses import dataclass
from datetime import date
from decimal import Decimal

@dataclass
class CreateContratoDto:
    fecha_inicio: date
    meses: int
    valor: int

    def get_attributes(cls):
        return[key.name for key in dataclasses.fields(CreateContratoDto)]