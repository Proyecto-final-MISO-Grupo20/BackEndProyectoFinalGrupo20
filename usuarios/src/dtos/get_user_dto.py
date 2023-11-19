from dataclasses import dataclass


@dataclass
class GetUserDto:
    id: int
    nombre: str
    tipo_documento: int
    documento: str
    email: str

    
