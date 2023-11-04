import dataclasses
from datetime import date
from dataclasses import dataclass

@dataclass
class CreateHabilidadDto:

    habilidades: list


    def get_attributes(self):
        return[key.name for key in dataclasses.fields(CreateHabilidadDto)]
