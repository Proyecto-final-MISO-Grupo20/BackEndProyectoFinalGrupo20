import pytest
from fastapi.exceptions import HTTPException

from .db_tests import init, close
from http import HTTPStatus
from src.services import utils_service


@pytest.mark.asyncio
async def test_validate_body_grades():
    await init()

    grades = {
        "comment": "Este es un comentario de prueba"
    }

    with pytest.raises(HTTPException) as exc_info:
        utils_service.validate_body(grades)

    assert exc_info.value.status_code == HTTPStatus.BAD_REQUEST

    await close()
