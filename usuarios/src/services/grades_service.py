from fastapi import HTTPException, Request
from http import HTTPStatus

from src.config import GRADES_SERVICE
from src.dtos import ResponseDto, GetGradesResponseDto
from src.services.utils_service import get_request, validate_response, validate_user_type


async def grades_of_candidate(request: Request, candidate_id: int, user_id: int):
    await validate_user_type(user_id, 'business')

    grades_response = await candidate_grades(candidate_id, request)

    return grades_response


async def grades_of_authenticated(request: Request, user_id: int):
    candidate = await validate_user_type(user_id, 'candidate')

    grades_response = await candidate_grades(candidate.id, request)

    return ResponseDto(grades_response, HTTPStatus.OK)


async def candidate_grades(candidate_id: int, request: Request):
    response_grades = await get_request(f'{GRADES_SERVICE}/grades/candidates/{candidate_id}', request)
    grades: GetGradesResponseDto = response_grades.get('body')
    validate_response(response_grades.get('status_code'), grades)

    return grades
