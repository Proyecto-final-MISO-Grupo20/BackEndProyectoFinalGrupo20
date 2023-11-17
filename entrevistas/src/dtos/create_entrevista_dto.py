import dataclasses
from dataclasses import dataclass
from datetime import date


@dataclass
class CreateEntrevistaDto:
    titulo: str
    fecha: date
    usuarios: list[int]

    @classmethod
    def get_attributes(cls):
        return [key.name for key in dataclasses.fields(CreateEntrevistaDto)]
