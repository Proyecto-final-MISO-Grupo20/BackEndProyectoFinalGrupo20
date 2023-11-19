import pytest

from .db_tests import init, close, delete_test_database
from http import HTTPStatus
from src.services import skills_service
from fastapi import HTTPException, Request
from src.models import Candidato, SkillCandidato


@pytest.mark.asyncio
async def test_add_skill_to_no_currently_created_user():
    await init()
    data = {"skill": 1, "nivel_dominio": 1}
    with pytest.raises(HTTPException) as exc_info:
        await skills_service.asociar_skill(data, 1)

    assert exc_info.value.status_code == 412
    await close()


@pytest.mark.asyncio
async def test_skill_to_candidate():
    await init()
    await test_add_skill_to_no_currently_created_user()
    candidato = Candidato(fecha_nacimiento=19990606, telefono=123,
                          pais="Colombia", ciudad="Bogotá",
                          usuarioId=1)

    await candidato.save()
    data = {"skill": 1, "nivel_dominio": 1}
    test_response = await skills_service.asociar_skill(data, 1)

    assert test_response.status_code == HTTPStatus.OK


@pytest.mark.asyncio
async def test_get_skills_of_candidate():
    await init()
    skills_list = await SkillCandidato.list(1)

    assert skills_list[0].skillId == 1


@pytest.mark.asyncio
async def test_get_skills_of_candidate_None():
    await init()
    skills_list = await SkillCandidato.list(None)

    assert len(skills_list) == 0

@pytest.mark.asyncio
async def test_add_skill_to_candidate_bad_request():

    data = {"skill": 2}

    with pytest.raises(HTTPException) as exc_info:
        await skills_service.asociar_skill(data, 1)

    assert exc_info.value.status_code == HTTPStatus.BAD_REQUEST
    assert exc_info.value.detail == "The request not contains all required data"


@pytest.mark.asyncio
async def test_get_skills_of_candidate_with_invalid_user():
    with pytest.raises(HTTPException) as exc_info:
        await skills_service.skills_of_candidate(Request, 1, 0)

    exception = exc_info.value
    assert exception.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.asyncio
async def test_get_skills_of_candidate_with_a_candidate_user():
    with pytest.raises(HTTPException) as exc_info:
        await skills_service.skills_of_candidate(Request, 2, 1)

    exception = exc_info.value
    assert exception.status_code == HTTPStatus.FORBIDDEN

    await delete_test_database()
