from dataclasses import dataclass
from .grades_dto import GradesDto


@dataclass
class GetGradesResponseDto:
    grades: list[GradesDto]
