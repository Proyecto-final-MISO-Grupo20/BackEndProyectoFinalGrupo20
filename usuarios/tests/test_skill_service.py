import pytest

from .db_tests import init, close
from http import HTTPStatus
from src.services import skill_service
from fastapi import HTTPException, Request
from src.models import Candidato


@pytest.mark.asyncio
async def test_asociar_error_servicio():
    await init()
    data = {"skill": 1, "nivel_dominio": 1}
    with pytest.raises(HTTPException) as exc_info:
        await skill_service.asociar_skill(data, 1)

    assert exc_info.value.status_code == 412
    await close()


@pytest.mark.asyncio
async def test_asociar():
    await init()
    await test_asociar_error_servicio()
    candidato = Candidato(fecha_nacimiento=19990606, telefono=123,
                          pais="Colombia", ciudad="Bogotá",
                          usuarioId=1)

    await candidato.save()
    data = {"skill": 1, "nivel_dominio": 1}
    test_response = await skill_service.asociar_skill(data, 1)

    assert test_response.status_code == HTTPStatus.OK


@pytest.mark.asyncio
async def test_get_skills_of_candidate_with_invalid_user():

    with pytest.raises(HTTPException) as exc_info:
        await skill_service.skills_of_candidate(Request, 1, 0)

    exception = exc_info.value
    assert exception.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.asyncio
async def test_get_skills_of_candidate_without_skills():

    with pytest.raises(HTTPException) as exc_info:
        await skill_service.skills_of_candidate(Request, 2, 1)

    exception = exc_info.value
    assert exception.status_code == HTTPStatus.NOT_FOUND

    await close()
