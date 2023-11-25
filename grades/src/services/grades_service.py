from fastapi import HTTPException, Request
from http import HTTPStatus

from src.dtos import ResponseDto, GetGradesResponseDto, CreateGradesResponseDto
from src.models import Grades
from src.services.projects_service import validate_project, get_project
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


async def get_candidate_grades(request: Request, candidate_id: int, user_id: int) -> ResponseDto:
    await validate_user_type(request, user_id, 'business')
    await validate_user_type(request, candidate_id, 'candidate')

    grades_response = await get_grades(request, candidate_id)

    return ResponseDto(grades_response, HTTPStatus.OK)


async def get_authenticated_candidate_grades(request: Request, candidate_id: int) -> ResponseDto:
    await validate_user_type(request, candidate_id, 'candidate')

    grades_response = await get_grades(request, candidate_id)

    return ResponseDto(grades_response, HTTPStatus.OK)


async def get_grades(request: Request, candidate_id: int):
    try:
        candidate_grades = await Grades.find_by_candidate_id(candidate_id)

        if not candidate_grades:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                                detail='The candidate with the given ID does not have any project grades')

        grades_response = []
        for candidate_grade in candidate_grades:
            project = await get_project(request, candidate_grade.project_id)
            grades_response.append(GetGradesResponseDto(
                candidate_grade.id, candidate_grade.grade, candidate_grade.comment, project
            ))

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED, detail=f'{exception}')

    return grades_response
