from enum import Enum


class EstadoOferta(Enum):
    DISPONIBLE: str = 'DISPONIBLE'
    ASIGNADO: str = 'ASIGNADO'
    EVALUANDO: str = 'EVALUANDO'
    CONTRATADO: str = 'CONTRATADO'
    FINALIZADO: str = 'FINALIZADO'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
