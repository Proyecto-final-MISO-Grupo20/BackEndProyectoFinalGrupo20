import pytest
from httpx import request

from src.models import Usuario, Candidato
from .db_tests import init, close, delete_test_database
from http import HTTPStatus
from src.services import candidate_service, business_service
from fastapi.exceptions import HTTPException


@pytest.mark.asyncio
async def test_get_candidates_invalid_user():
    await init()
    with pytest.raises(HTTPException) as exc_info:
        await candidate_service.get_candidates(request, None)

    assert exc_info.value.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.asyncio
async def test_get_candidates_empty_list():
    create_business_response = await business_service.create_empresa({
        "nombre": "John Doe",
        "tipo_documento": 1,
        "documento": 9876543,
        "username": "company",
        "password": "fakepassword",
        "email": "example@example.com",
        "segmentoId": 1,
        "tipoEmpresaId": 1,
        "direccion": "Fake Address 123",
        "pais": "Fake Country",
        "ciudad": "Fake City"
    })
    user = await Usuario.get_by_username(create_business_response.body.username)
    with pytest.raises(HTTPException) as exc_info:
        await candidate_service.get_candidates(request, user.id)

    assert exc_info.value.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.asyncio
async def test_get_candidates():
    candidate = Candidato(fecha_nacimiento=19990606, telefono=123,
                          pais="Colombia", ciudad="Bogotá",
                          usuarioId=10)
    await candidate.save()
    with pytest.raises(HTTPException) as exc_info:
        await candidate_service.get_candidates(request, '1')

    assert exc_info.value.status_code == HTTPStatus.NOT_FOUND
    assert (exc_info.value.detail ==
            'The user with the requested ID does not exist or there is an issue with the database relations')


@pytest.mark.asyncio
async def test_create_candidate():
    test_response = await candidate_service.create_candidato({
        "nombre": "Juan Jose Ochoa Ortiz",
        "tipo_documento": 1,
        "documento": 1234567,
        "username": "juanochoa8",
        "password": "password",
        "email": "ejemplo@ejemplo.com",
        "fecha_nacimiento": 20230601,
        "telefono": 123456,
        "pais": "Colombia",
        "ciudad": "Bogota"
    })

    assert test_response.status_code == HTTPStatus.CREATED


@pytest.mark.asyncio
async def test_create_candidate_with_missing_fields():
    await init()

    with pytest.raises(HTTPException) as exc_info:
        await candidate_service.create_candidato({
            "nombre": "Juan Jose Ochoa Ortiz",
            "tipo_documento": 1,
            "documento": "1234567",
            "username": "juanochoa",
            "password": "password",
            "email": "ejemplo@ejemplo.com",
            "fecha_nacimiento": 20230601,
            "telefono": 123456,
            "pais": "Colombia"
        })

    # Verifica el código de estado HTTP de la excepción
    assert exc_info.value.status_code == 400

    await close()


@pytest.mark.asyncio
async def test_create_candidate_with_invalid_username():
    await init()

    with pytest.raises(HTTPException) as exc_info:
        await candidate_service.create_candidato({
            "nombre": "John Doe",
            "tipo_documento": 1,
            "documento": 45678,
            "username": "maxlengthofcolumnreacheditslimitof25characters",
            "password": "password",
            "email": "johndoe@ejemplo.com",
            "fecha_nacimiento": 20230601,
            "telefono": 123456,
            "pais": "USA",
            "ciudad": "Miami"
        })

    # Verifica el código de estado HTTP de la excepción
    assert exc_info.value.status_code == 500

    await close()


@pytest.mark.asyncio
async def test_create_candidate_duplicated_username():
    await init()

    # Primera llamada para crear un usuario
    await candidate_service.create_candidato({
        "nombre": "Juan Jose Ochoa Ortiz",
        "tipo_documento": 1,
        "documento": "1234567",
        "username": "juanochoa1",
        "password": "password",
        "email": "ejemplo@ejemplo.com",
        "fecha_nacimiento": 20230601,
        "telefono": 123456,
        "pais": "Colombia",
        "ciudad": "Bogota"
    })

    # Segunda llamada para crear un usuario con el mismo username

    test_response = await candidate_service.create_candidato({
        "nombre": "Otro Nombre",
        "tipo_documento": 2,
        "documento": "1234567",
        "username": "juanochoa1",
        "password": "password2",
        "email": "otro@ejemplo.com",
        "fecha_nacimiento": 20230602,
        "telefono": 654321,
        "pais": "Colombia",
        "ciudad": "Medellin"
    })

    # Verifica que se haya lanzado una excepción HTTPException con código 400 (Bad Request)
    assert test_response.status_code == 400

    await close()


@pytest.mark.asyncio
async def test_get_candidates_with_unauthorized_user():
    with pytest.raises(HTTPException) as exc_info:
        await candidate_service.get_candidates(request, "2")

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_not_found_username():
    await init()
    test_response = await Usuario.get_by_username('no_user')

    assert test_response is None

    await close()


@pytest.mark.asyncio
async def test_get_user_by_id():
    await init()
    user = await Usuario.get_by_username('juanochoa8')

    test_response = await Usuario.get_by_id(user.id)

    assert test_response.id == user.id

    await close()


@pytest.mark.asyncio
async def test_not_found_id():
    await init()
    test_response = await Usuario.get_by_id(123)

    assert test_response is None


@pytest.mark.asyncio
async def test_get_list_of_candidates():
    candidates = await Candidato.list()

    assert candidates is not None

    await delete_test_database()
