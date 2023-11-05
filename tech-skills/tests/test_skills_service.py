import pytest
from fastapi import HTTPException

from .db_tests import init, close
from http import HTTPStatus
from src.services import skills_service


@pytest.mark.asyncio
async def test_crear_idioma():
    await init()

    test_response = await skills_service.create_skill({
        "nombre": "Español",
        "tipo": "IDIOMA"
    })

    assert test_response.status_code == HTTPStatus.CREATED


@pytest.mark.asyncio
async def test_error_al_crear_skill_sin_todos_los_campos():

    with pytest.raises(HTTPException) as exc_info:
        await skills_service.create_skill({
            "nombre": "Español"
        })

    exception = exc_info.value
    assert exception.status_code == HTTPStatus.BAD_REQUEST
    await close()


@pytest.mark.asyncio
async def test_listar_idiomas():
    test_response = await skills_service.listar_skills("IDIOMA")

    assert test_response.status_code == HTTPStatus.OK


@pytest.mark.asyncio
async def test_listar_tipo_de_skill_no_encontrada():
    test_response = await skills_service.listar_skills("HABILIDAD")

    assert test_response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.asyncio
async def test_listar_skill_de_tipo_erroneo():
    with pytest.raises(HTTPException) as exc_info:
        await skills_service.listar_skills("INVALID_TYPE")

    exception = exc_info.value
    assert exception.status_code == HTTPStatus.PRECONDITION_FAILED
    assert exception.detail == "Invalid skill type, it must be HERRAMIENTA, HABILIDAD or IDIOMA"
    await close()
