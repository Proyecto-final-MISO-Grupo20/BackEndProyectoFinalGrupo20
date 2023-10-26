import pytest

from .db_tests import init, close
from http import HTTPStatus
from src.services import habilidades_service
from fastapi.exceptions import HTTPException
from src.models import Habilidades, Candidato
from src.dtos import CreateHabilidadDto




@pytest.mark.asyncio
async def test_listar_vacio():
    await init()
    test_response = await habilidades_service.listar_habilidades()
    
    assert test_response.status_code == HTTPStatus.BAD_REQUEST

    await close()

@pytest.mark.asyncio
async def test_listar():
    await init()
    habilidades = Habilidades(habilidad = 'prueba', tipoHabilidad = 1)
    await habilidades.save()
    test_response = await habilidades_service.listar_habilidades()
    
    assert test_response.status_code == HTTPStatus.CREATED

    await close()

@pytest.mark.asyncio
async def test_crear():
    await init()
    candidato = Candidato(fecha_nacimiento=19990606, telefono=123,
                            pais="Colombia", ciudad="Bogotá",
                            usuarioId=1)

    await candidato.save()  
    data = CreateHabilidadDto([1, 2, 3])
    test_response = await habilidades_service.create_habilidad(data, 1)
    
    assert test_response.status_code == HTTPStatus.CREATED

    await close()



