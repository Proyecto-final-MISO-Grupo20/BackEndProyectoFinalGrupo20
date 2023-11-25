from dataclasses import dataclass


@dataclass
class GetProjectDto:

    id = int
    nombre = str
    descripcion = str
    codigo = int
    empresaId = int
