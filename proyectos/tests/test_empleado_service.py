import pytest

from .db_tests import init, close
from http import HTTPStatus
from src.services import empleado_service
from src.models import Proyecto_Empleado
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

@pytest.mark.asyncio
async def test_asociar_empleado_sin_proyecto():
    await init() 
    data = {"empleadoId":1}
    with pytest.raises(HTTPException) as exc_info:
        await empleado_service.asociar_empleado_proyecto(data)
    
    assert exc_info.value.status_code == 400
    await close()

@pytest.mark.asyncio
async def test_asociar_empleado_proyecto_repetido():
    await init() 
    proyecto_empleado = Proyecto_Empleado(empleadoId = 1, proyectoId = 1)

    await proyecto_empleado.save()  
    data = {"empleadoId":1, "proyectoId":1}
    test_response = await empleado_service.asociar_empleado_proyecto(data)
    
    assert test_response.status_code == HTTPStatus.BAD_REQUEST
    await close()

@pytest.mark.asyncio
async def test_asociar_empleado_proyecto():
    await init() 
    data = {"empleadoId":1, "proyectoId":2}

    test_response = await empleado_service.asociar_empleado_proyecto(data)

    # Verifica que se haya creado el empleado
    assert test_response.status_code == HTTPStatus.OK

    await close()