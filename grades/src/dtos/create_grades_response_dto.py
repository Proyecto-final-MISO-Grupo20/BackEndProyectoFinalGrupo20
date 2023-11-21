from dataclasses import dataclass


@dataclass
class CreateGradesResponseDto:
    id: int
    grade: str
    comment: str
    candidate_id: int
    project_id: int
