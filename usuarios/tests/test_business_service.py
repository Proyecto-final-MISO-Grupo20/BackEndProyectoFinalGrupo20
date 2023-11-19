import pytest

from src.models import TipoEmpresa, Segmento, Empresa
from src.services import business_service
from .db_tests import init, close, delete_test_database
from http import HTTPStatus
from fastapi.exceptions import HTTPException


@pytest.mark.asyncio
async def test_create_empresa():
    await init()

    test_response = await business_service.create_empresa({
        "nombre": "Juan Jose Ochoa Ortiz",
        "tipo_documento": 1,
        "documento": 1234567,
        "username": "empresa",
        "password": "password",
        "email": "ejemplo@ejemplo.com",
        "segmentoId": 1,
        "tipoEmpresaId": 1,
        "direccion": "Prueba 166",
        "pais": "Colombia",
        "ciudad": "Bogotá"
    })

    assert test_response.status_code == HTTPStatus.CREATED

    await close()


@pytest.mark.asyncio
async def test_create_empresa_faltan_campos():
    await init()

    with pytest.raises(HTTPException) as exc_info:
        await business_service.create_empresa({
            "nombre": "Juan Jose Ochoa Ortiz",
            "tipo_documento": 1,
            "documento": "1234567",
            "username": "juanochoa",
            "password": "password",
            "email": "ejemplo@ejemplo.com"
        })

    # Verifica el código de estado HTTP de la excepción
    assert exc_info.value.status_code == 400

    await close()


@pytest.mark.asyncio
async def test_create_empresa_con_username_repetido():
    await init()

    # Primera llamada para crear un usuario
    await business_service.create_empresa({
        "nombre": "Juan Jose Ochoa Ortiz",
        "tipo_documento": 1,
        "documento": "1234567",
        "username": "empresa2",
        "password": "password",
        "email": "ejemplo@ejemplo.com",
        "segmentoId": 1,
        "tipoEmpresaId": 1,
        "direccion": "Prueba 166",
        "pais": "Colombia",
        "ciudad": "Bogotá"
    })

    # Segunda llamada para crear un usuario con el mismo username

    with pytest.raises(HTTPException) as exc_info:
        await business_service.create_empresa({
            "nombre": "Juan Jose Ochoa Ortiz",
            "tipo_documento": 1,
            "documento": "1234567",
            "username": "empresa2",
            "password": "password",
            "email": "ejemplo@ejemplo.com",
            "segmentoId": 1,
            "tipoEmpresaId": 1,
            "direccion": "Prueba 166",
            "pais": "Colombia",
            "ciudad": "Bogotá"
        })

    # Verifica que se haya lanzado una excepción HTTPException con código 400 (Bad Request)
    assert exc_info.value.status_code == 400

    await close()


@pytest.mark.asyncio
async def test_not_found_business_types():
    await init()
    test_response = await business_service.get_business_types()

    assert test_response.status_code == HTTPStatus.NOT_FOUND

    await close()


@pytest.mark.asyncio
async def test_get_business_types():
    await init()
    segmento = TipoEmpresa(tipo='Privada')
    await segmento.save()
    test_response = await business_service.get_business_types()

    assert test_response.status_code == HTTPStatus.OK

    await close()


@pytest.mark.asyncio
async def test_not_found_segments():
    await init()
    test_response = await business_service.get_business_segments()

    assert test_response.status_code == HTTPStatus.NOT_FOUND

    await close()


@pytest.mark.asyncio
async def test_get_segments():
    await init()
    segmento = Segmento(segmento='prueba')
    await segmento.save()
    test_response = await business_service.get_business_segments()

    assert test_response.status_code == HTTPStatus.OK


@pytest.mark.asyncio
async def test_get_business_by_user_id():

    test_response = await Empresa.find_by_user_id(1)
    assert test_response.id == 1


@pytest.mark.asyncio
async def test_not_found_business_by_user_id():
    await init()
    test_response = await Empresa.find_by_user_id(123)

    assert test_response is None

    await delete_test_database()