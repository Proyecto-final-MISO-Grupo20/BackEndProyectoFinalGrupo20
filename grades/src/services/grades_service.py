from fastapi import HTTPException, Request
from http import HTTPStatus

from src.dtos import ResponseDto
from src.dtos.create_grades_response_dto import CreateGradesResponseDto
from src.models import Grades
from src.services.projects_service import validate_project
from src.services.user_service import validate_user_type
from src.services.utils_service import validate_body


async def create_grades(request: Request, candidate_id: int, project_id: int, user_id: int) -> ResponseDto:
    await validate_user_type(request, user_id, 'business')
    await validate_user_type(request, candidate_id, 'candidate')
    await validate_project(request, project_id)

    data = await request.json()
    validate_body(data)

    try:
        grades = Grades(
            grade=data.get('grade'), comment=data.get('comment'), candidate_id=candidate_id,project_id=project_id
        )
        await grades.save()
        body = CreateGradesResponseDto(
            grades.id, grades.grade, grades.comment, grades.candidate_id, grades.project_id
        )

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED,
                            detail=f'{exception}')

    return ResponseDto(body, HTTPStatus.CREATED)
