import pytest

from .db_tests import init, close
from http import HTTPStatus
from src.services import herramientas_service
from fastapi.exceptions import HTTPException
from src.models import Herramientas, Candidato
from src.dtos import CreateHerramientaDto



@pytest.mark.asyncio
async def test_listar_vacio():
    await init()
    test_response = await herramientas_service.listar_herramientas()
    
    assert test_response.status_code == HTTPStatus.BAD_REQUEST

    await close()

@pytest.mark.asyncio
async def test_listar():
    await init()
    herramientas = Herramientas(herramienta = 'prueba')
    await herramientas.save()
    test_response = await herramientas_service.listar_herramientas()
    
    assert test_response.status_code == HTTPStatus.CREATED

    await close()

@pytest.mark.asyncio
async def test_crear():
    await init()
    candidato = Candidato(fecha_nacimiento=19990606, telefono=123,
                            pais="Colombia", ciudad="Bogotá",
                            usuarioId=1)

    await candidato.save()  
    data = CreateHerramientaDto([1, 2, 3])
    test_response = await herramientas_service.create_herramienta(data, 1)
    
    assert test_response.status_code == HTTPStatus.CREATED

    await close()


