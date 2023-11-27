from dataclasses import dataclass


@dataclass
class CreateProjectDto:

    id: int
    nombre: str
    descripcion: str
    codigo: int
    empresaId: int
