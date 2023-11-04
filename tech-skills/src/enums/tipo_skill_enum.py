from enum import Enum


class TipoSkill(Enum):
    HABILIDAD: str = 'HABILIDAD'
    HERRAMIENTA: str = 'HERRAMIENTA'
    IDIOMA: str = 'IDIOMA'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
