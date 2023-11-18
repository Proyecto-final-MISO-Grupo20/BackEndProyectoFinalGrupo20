from dataclasses import dataclass


@dataclass
class GetUserDto:
    nombre: str
    tipo_documento: int
    documento: str
    email: str

    
