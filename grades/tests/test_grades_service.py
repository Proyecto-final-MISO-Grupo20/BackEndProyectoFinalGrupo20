import pytest
from fastapi.exceptions import HTTPException
from httpx import request

from src.models import Grades
from src.services.grades_service import get_grades
from .db_tests import init, delete_test_database
from http import HTTPStatus
from src.services import grades_service

UN_COMENTARIO_DE_PRUEBA = "Este es un comentario de prueba"


@pytest.mark.asyncio
async def test_validate_user_type_none_user():
    await init()

    with pytest.raises(HTTPException) as exc_info:
        await grades_service.create_grades(request, 1, 1, None)

    assert exc_info.value.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.asyncio
async def test_validate_save_grades():
    await init()

    data = {
        "grade": "5",
        "comment": UN_COMENTARIO_DE_PRUEBA
    }

    grades = Grades(
        grade=data.get('grade'), comment=data.get('comment'), candidate_id=1, project_id=1
    )

    await grades.save()
    assert grades.comment == UN_COMENTARIO_DE_PRUEBA


@pytest.mark.asyncio
async def test_find_grades_by_candidate_id():
    candidate_grades = await Grades.find_by_candidate_id(1)

    assert candidate_grades[0].comment == UN_COMENTARIO_DE_PRUEBA


@pytest.mark.asyncio
async def test_find_grades_by_candidate_id_invalid_candidate():
    candidate_grades = await Grades.find_by_candidate_id(None)

    assert candidate_grades == []


@pytest.mark.asyncio
async def test_get_grades_service():

    with pytest.raises(HTTPException) as exc_info:
        await get_grades(request, 1)

    assert exc_info.value.status_code == HTTPStatus.PRECONDITION_FAILED


@pytest.mark.asyncio
async def test_get_grades_service_no_found_candidate():

    with pytest.raises(HTTPException) as exc_info:
        await get_grades(request, 123)

    assert exc_info.value.status_code == HTTPStatus.PRECONDITION_FAILED

    await delete_test_database()
