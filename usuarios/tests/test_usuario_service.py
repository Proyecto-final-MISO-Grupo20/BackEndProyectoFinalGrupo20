import pytest

from .db_tests import init, close
from http import HTTPStatus
from src.services import usuario_service
from fastapi.exceptions import HTTPException


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

    with pytest.raises(HTTPException) as exc_info:
        await usuario_service.create_candidato({
            "nombre": "Juan Jose Ochoa Ortiz",
            "tipoDocumento": 1,
            "documento": "1234567",
            "username": "juanochoa",
            "password": "password",
            "email": "ejemplo@ejemplo.com",
            "fechaNacimiento": 20230601,
            "telefono": 123456,
            "pais": "Colombia"
        })

    # Verifica el código de estado HTTP de la excepción
    assert exc_info.value.status_code == 400    

@pytest.mark.asyncio
async def test_create_usuario_con_username_repetido():
    await init()

    # Primera llamada para crear un usuario
    await usuario_service.create_candidato({
        "nombre": "Juan Jose Ochoa Ortiz",
        "tipoDocumento": 1,
        "documento": "1234567",
        "username": "juanochoa1",
        "password": "password",
        "email": "ejemplo@ejemplo.com",
        "fechaNacimiento": 20230601,
        "telefono": 123456,
        "pais": "Colombia",
        "ciudad": "Bogota"
    })

    # Segunda llamada para crear un usuario con el mismo username
    with pytest.raises(HTTPException) as exc_info:
        await usuario_service.create_candidato({
            "nombre": "Otro Nombre",
            "tipoDocumento": 2,
            "documento": "1234567",
            "username": "juanochoa1",
            "password": "password2",
            "email": "otro@ejemplo.com",
            "fechaNacimiento": 20230602,
            "telefono": 654321,
            "pais": "Colombia",
            "ciudad": "Medellin"
        })

    # Verifica que se haya lanzado una excepción HTTPException con código 400 (Bad Request)
    assert exc_info.value.status_code == 400
