import pytest

from .db_tests import init, close
from http import HTTPStatus
from src.services import proyecto_service
from src.models import Proyecto
from fastapi.exceptions import HTTPException

@pytest.mark.asyncio
async def test_create_proyecto_con_usuario_mal():
    await init()

    # Se crea el proyecto con una empresa que no tiene usuario asociado tipo empresa
    test_response = await proyecto_service.create_proyecto({
                                                                "nombre": "Prueba",
                                                                "descripcion": "Prueba",
                                                                "codigo": 1234567
                                                            }, 2)
    
    assert test_response.status_code == HTTPStatus.BAD_REQUEST

    await close()

@pytest.mark.asyncio
async def test_create_proyecto():
    await init()

    # Se crea el proyecto con una empresa correcta
    test_response = await proyecto_service.create_proyecto({
                                                                "nombre": "Prueba",
                                                                "descripcion": "Prueba",
                                                                "codigo": 1234567
                                                            }, 1)

    # Verifica que se haya lanzado una excepción HTTPException con código 400 (Bad Request)
    assert test_response.status_code == HTTPStatus.CREATED

    await close()

@pytest.mark.asyncio
async def test_listar_proyectos_con_usuario_mal():
    await init()

    # Se crea el proyecto con una empresa que no tiene usuario asociado tipo empresa
    test_response = await proyecto_service.list_proyectos(2)
    
    assert test_response.status_code == HTTPStatus.BAD_REQUEST

    await close()

@pytest.mark.asyncio
async def test_listar_proyectos():
    await init()
    await test_create_proyecto()
    
    # Se crea el proyecto con una empresa que no tiene usuario asociado tipo empresa
    test_response = await proyecto_service.list_proyectos(1)
    
    assert test_response.status_code == HTTPStatus.OK

    await close()


@pytest.mark.asyncio
async def test_get_project():
    await init()
    await test_create_proyecto()

    test_response = await proyecto_service.get_project(1, 1)

    assert test_response.status_code == HTTPStatus.OK

    await close()


@pytest.mark.asyncio
async def test_get_project_precondition_failed():
    await init()
    await test_create_proyecto()

    with pytest.raises(HTTPException) as exc_info:
        await proyecto_service.get_project('', 1)

    assert exc_info.value.status_code == HTTPStatus.PRECONDITION_FAILED

    await close()


# @pytest.mark.asyncio
# async def test_get_project_not_found_user():
#     await init()
#     await test_create_proyecto()
#
#     test_response = await proyecto_service.get_project(1, 123)
#
#     assert test_response.status_code == HTTPStatus.BAD_REQUEST
#
#     await close()


@pytest.mark.asyncio
async def test_get_project_not_found_project():
    await init()
    await test_create_proyecto()

    test_response = await Proyecto.find_by_id(123)

    assert test_response is None

    await close()
