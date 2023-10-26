import dataclasses
from datetime import date
from dataclasses import dataclass

@dataclass
class CreateHerramientaDto:

    herramientas: list


    def get_attributes(self):
        return[key.name for key in dataclasses.fields(CreateHerramientaDto)]
