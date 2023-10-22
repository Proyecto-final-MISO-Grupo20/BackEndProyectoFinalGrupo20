from enum import Enum

class UsuarioSize(Enum):
    LARGE: str = 'LARGE'
    MEDIUM: str = 'MEDIUM'
    SMALL: str = 'SMALL'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_ 