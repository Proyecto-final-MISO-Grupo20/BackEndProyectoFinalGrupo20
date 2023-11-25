from dataclasses import dataclass

from .get_project_dto import GetProjectDto


@dataclass
class GetGradesResponseDto:
    id: int
    grade: str
    comment: str
    project: [GetProjectDto]
