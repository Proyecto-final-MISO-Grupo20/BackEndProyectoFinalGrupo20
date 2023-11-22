import pytest
from http import HTTPStatus


from .db_tests import init, delete_test_database
from src.services import utils_service, business_service, candidate_service
from fastapi.exceptions import HTTPException


@pytest.mark.asyncio
async def test_validate_user_type_none_user():
    await init()

    with pytest.raises(HTTPException) as exc_info:
        await utils_service.validate_user_type(None, 'business')

    assert exc_info.value.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.asyncio
async def test_validate_user_type_business():
    await init()

    await business_service.create_empresa({
        "nombre": "John Doe",
        "tipo_documento": 1,
        "documento": 9876543,
        "username": "company",
        "password": "fakepassword",
        "email": "example@example.com",
        "segmentoId": 1,
        "tipoEmpresaId": 1,
        "direccion": "Fake Address 123",
        "pais": "Fake Country",
        "ciudad": "Fake City"
    })

    business = await utils_service.validate_user_type(1, 'business')

    assert business.id == 1


@pytest.mark.asyncio
async def test_validate_user_type_candidate():
    await init()

    await candidate_service.create_candidato({
        "nombre": "Jane Smith",
        "tipo_documento": 2,
        "documento": 5678901,
        "username": "janesmith",
        "password": "password",
        "email": "jane@example.com",
        "fecha_nacimiento": 20230601,
        "telefono": 123456,
        "pais": "United States",
        "ciudad": "New York"
    })

    candidate = await utils_service.validate_user_type(2, 'candidate')

    assert candidate.id == 1


@pytest.mark.asyncio
async def test_validate_user_type_not_forbidden_user_type():
    await init()

    with pytest.raises(HTTPException) as exc_info:
        await utils_service.validate_user_type(222, '')

    assert exc_info.value.status_code == HTTPStatus.FORBIDDEN

    await delete_test_database()
