import dataclasses
from dataclasses import dataclass
from datetime import date


@dataclass
class QualifyEntrevistaDto:
    id: int
    calificacion: int
    comentario: str

    @classmethod
    def get_attributes(cls):
        return [key.name for key in dataclasses.fields(QualifyEntrevistaDto)]
