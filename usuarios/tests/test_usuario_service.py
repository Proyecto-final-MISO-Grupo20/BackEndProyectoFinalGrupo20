import pytest

from .db_tests import init, close
from http import HTTPStatus
from src.services import usuario_service


@pytest.mark.asyncio
async def test_create_usuario():
    await init()

    test_response = await usuario_service.create_candidato({
            "nombre": "Juan Jose Ochoa Ortiz",
            "tipoDocumento": 1,
            "documento": 1234567,
            "username": "juanochoa",
            "password": "password",
            "email": "ejemplo@ejemplo.com",
            "fechaNacimiento": 20230601,
            "telefono": 123456,
            "pais": "Colombia",
            "ciudad": "Bogota"
        })

    assert test_response.status_code == HTTPStatus.CREATED

@pytest.mark.asyncio
async def test_create_usuario_faltan_campos():
    await init()

    test_response = await usuario_service.create_candidato({
            "nombre": "Juan Jose Ochoa Ortiz",
            "tipoDocumento": 1,
            "documento": 1234567,
            "username": "juanochoa",
            "password": "password",
            "email": "ejemplo@ejemplo.com",
            "fechaNacimiento": 20230601,
            "telefono": 123456,
            "pais": "Colombia"
        })

    assert test_response.status_code == HTTPStatus.BAD_REQUEST

