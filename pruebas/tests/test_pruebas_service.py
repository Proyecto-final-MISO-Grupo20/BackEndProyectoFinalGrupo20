import pytest
from fastapi import HTTPException

from .db_tests import init, close
from http import HTTPStatus
from src.services import prueba_service


@pytest.mark.asyncio
async def test_postular_candidato_faltan_campos():
    await init()

    with pytest.raises(HTTPException) as exc_info:
        await prueba_service.postular_candidato({"oferta": 1}, 1)

    # Verifica el código de estado HTTP de la excepción
    assert exc_info.value.status_code == 400 

    await close() 

@pytest.mark.asyncio
async def test_postular_candidato_ok():
    await init()

    test_response = await prueba_service.postular_candidato({"ofertaId": 1}, 1)

    assert test_response.status_code == 200

    await close() 

@pytest.mark.asyncio
async def test_postular_candidato_ya_existe():
    await init()
    await prueba_service.postular_candidato({"ofertaId": 2}, 1)
    test_response = await prueba_service.postular_candidato({"ofertaId": 2}, 1)

    # Verifica que se haya lanzado una excepción HTTPException con código 400 (Bad Request)
    assert test_response.status_code == 400

    await close() 

@pytest.mark.asyncio
async def test_registrar_prueba_ok():
    await init()

    test_response = await prueba_service.registrar_prueba({"postulacionId": 1,
                                                           "calificacion": 10,
                                                           "comentario": "Excelente",
                                                           "tipo": 1,
                                                           "nombre": "Prueba tecnica"
                                                           })

    assert test_response.status_code == 201

    await close() 