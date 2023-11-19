import dataclasses
from dataclasses import dataclass


@dataclass
class CreateEmpresaDto:
    nombre: str
    tipo_documento: int
    documento: str
    username: str
    password: str
    email: str
    segmentoId: int
    tipoEmpresaId: int
    direccion = str
    pais = str
    ciudad = str

    def get_attributes(self):
        return [key.name for key in dataclasses.fields(CreateEmpresaDto)]
