import pytest
from fastapi import HTTPException

from .db_tests import init, close
from http import HTTPStatus
from src.services import offers_service


@pytest.mark.asyncio
async def test_crear_oferta():
    await init()

    test_response = await offers_service.create_offer({
        "perfil": "Desarrollador de backend",
        "skills": [
            {
                "skill_id": "1",
                "dominio": "5"
            },
            {
                "skill_id": "3",
                "dominio": "4"
            }
        ]
    }, 1, 1)
 
    assert test_response.status_code == HTTPStatus.CREATED


@pytest.mark.asyncio
async def test_actualizar_oferta():
    await init()

    test_response = await offers_service.update_offer(1, 1)
 
    assert test_response.status_code == HTTPStatus.OK


@pytest.mark.asyncio
async def test_crear_oferta_usuario_no_autorizado():
    await init()

    test_response = await offers_service.create_offer({
        "perfil": "Desarrollador de backend",
        "skills": [
            {
                "skill_id": "1",
                "dominio": "5"
            },
            {
                "skill_id": "3",
                "dominio": "4"
            }
        ]
    }, 1, 0)

    assert test_response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.asyncio
async def test_error_al_crear_oferta_con_datos_incompletos():
    with pytest.raises(HTTPException) as exc_info:
        await offers_service.create_offer({
            "perfil": "Desarrollador de backend"
        }, 1, 1)

    exception = exc_info.value
    assert exception.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.asyncio
async def test_error_al_crear_oferta_con_datos_de_skills_incompletos():
    with pytest.raises(HTTPException) as exc_info:
        await offers_service.create_offer({
            "perfil": "Desarrollador de backend",
            "skills": [
                {
                    "skill_id": "1"
                }
            ]
        }, 1, 1)

    exception = exc_info.value
    assert exception.status_code == HTTPStatus.PRECONDITION_FAILED


@pytest.mark.asyncio
async def test_list_offers():
    test_response = await offers_service.list_offers()
 
    assert test_response.status_code == HTTPStatus.OK

@pytest.mark.asyncio
async def test_list_offers_by_project():
    test_response = await offers_service.list_offers_by_project(1)
 
    assert test_response.status_code == HTTPStatus.OK