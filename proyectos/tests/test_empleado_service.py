import pytest

from .db_tests import init, close
from http import HTTPStatus
from src.services import empleado_service
from src.models import Empleado, Empresa
from fastapi.exceptions import HTTPException

@pytest.mark.asyncio
async def test_create_empleado_con_usuario_mal():
    await init()

    # Se crea el proyecto con una empresa que no tiene usuario asociado tipo empresa
    test_response = await empleado_service.create_empleado({
                                                                "nombre": "Prueba",
                                                                "tipo_documento": 1,
                                                                "documento": "123456",
                                                                "cargo":"Prueba",
                                                                "email":"prueba@ejemplo.com"
                                                            }, 2)
    
    assert test_response.status_code == HTTPStatus.BAD_REQUEST

    await close()

@pytest.mark.asyncio
async def test_create_empleado():
    await init()

    # Se crea el proyecto con una empresa correcta
    test_response = await empleado_service.create_empleado({
                                                                "nombre": "Prueba",
                                                                "tipo_documento": 1,
                                                                "documento": "123456",
                                                                "cargo":"Prueba",
                                                                "email":"prueba@ejemplo.com"
                                                            }, 1)

    # Verifica que se haya creado el empleado
    assert test_response.status_code == HTTPStatus.CREATED

    await close()
