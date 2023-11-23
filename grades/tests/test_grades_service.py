import pytest
from fastapi.exceptions import HTTPException
from httpx import request

from .db_tests import init, delete_test_database
from http import HTTPStatus
from src.services import grades_service


@pytest.mark.asyncio
async def test_validate_user_type_none_user():
    await init()

    with pytest.raises(HTTPException) as exc_info:
        await grades_service.create_grades(request, 1, 1, None)

    assert exc_info.value.status_code == HTTPStatus.UNAUTHORIZED

    await delete_test_database()
