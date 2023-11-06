import dataclasses
from datetime import date
from dataclasses import dataclass

@dataclass
class AsociateEmpleadoDto:

    proyectoId: int
    empleadoId: int

    def get_attributes(self):
        return[key.name for key in dataclasses.fields(AsociateEmpleadoDto)]
