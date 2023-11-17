import pytest
from fastapi import HTTPException

from .db_tests import init, close
from http import HTTPStatus
from src.services import entrevistas_service

@pytest.mark.asyncio
async def test_crear_entrevista_sin_usuario():
    await init()

    test_response = await entrevistas_service.create_entrevista({
        "titulo": "Entrevista de prueba",
        "fecha": 20231201,
        "usuarios": [2,3]
    }, None)
 
    assert test_response.status_code == HTTPStatus.UNAUTHORIZED

    await close() 

@pytest.mark.asyncio
async def test_crear_entrevista_sin_titulo():
    await init()

    with pytest.raises(HTTPException) as exc_info:
        await entrevistas_service.create_entrevista({
        "fecha": 20231201,
        "usuarios": [2,3]
    }, None)

    # Verifica el código de estado HTTP de la excepción
    assert exc_info.value.status_code == 400

    await close() 

@pytest.mark.asyncio
async def test_crear_entrevista():
    await init()

    test_response = await entrevistas_service.create_entrevista({
        "titulo": "Entrevista de prueba",
        "fecha": 20231201,
        "usuarios": [2,3]
    }, 1)
 
    assert test_response.status_code == HTTPStatus.CREATED

    await close() 

@pytest.mark.asyncio
async def test_calificar_entrevista_sin_usuario():
    await init()

    test_response = await entrevistas_service.qualify_entrevista({
        "id":1,
        "calificacion": 5,
        "comentario": "Este es un comentario de prueba."
    }, None)
 
    assert test_response.status_code == HTTPStatus.UNAUTHORIZED

    await close() 

@pytest.mark.asyncio
async def test_calificar_entrevista_sin_comentario():
    await init()


    with pytest.raises(HTTPException) as exc_info:
        await entrevistas_service.qualify_entrevista({
        "id": 1,
        "calificacion": 5
    }, 1)

    # Verifica el código de estado HTTP de la excepción
    assert exc_info.value.status_code == 400

    await close() 

@pytest.mark.asyncio
async def test_calificar_entrevista_no_existe():
    await init()

    test_response = await entrevistas_service.qualify_entrevista({
        "id":5,
        "calificacion": 5,
        "comentario": "Este es un comentario de prueba."
    }, 1)

    # Verifica el código de estado HTTP de la excepción
    assert test_response.status_code == HTTPStatus.NOT_FOUND

    await close() 


@pytest.mark.asyncio
async def test_calificar_entrevista():
    await init()

    test_response = await entrevistas_service.qualify_entrevista({
        "id": 1,
        "calificacion": 5,
        "comentario": "Este es un comentario de prueba."
    }, 1)
 
    assert test_response.status_code == HTTPStatus.OK

    await close() 

@pytest.mark.asyncio
async def test_listar_entrevista_vacio():
    await init()

    test_response = await entrevistas_service.list_entrevistas_by_user(5)
 
    assert test_response.status_code == HTTPStatus.NOT_FOUND

    await close() 

@pytest.mark.asyncio
async def test_listar_entrevista():
    await init()

    test_response = await entrevistas_service.list_entrevistas_by_user(2)
 
    assert test_response.status_code == HTTPStatus.OK

    await close() 