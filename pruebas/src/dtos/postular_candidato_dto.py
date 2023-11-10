import dataclasses
from datetime import date
from dataclasses import dataclass

@dataclass
class PostularCandidatoDto:

    ofertaId: int

    def get_attributes(cls):
        return[key.name for key in dataclasses.fields(PostularCandidatoDto)]
