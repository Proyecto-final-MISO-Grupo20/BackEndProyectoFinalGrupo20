import pytest

from .db_tests import init, close
from http import HTTPStatus
from src.services import proyecto_service
from src.models import Empresa
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
