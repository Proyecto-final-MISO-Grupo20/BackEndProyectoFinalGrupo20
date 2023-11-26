from dataclasses import dataclass

from .get_project_dto import CreateProjectDto


@dataclass
class GradesDto:
    id = int
    grade = int
    comment = str
    project = [CreateProjectDto]
