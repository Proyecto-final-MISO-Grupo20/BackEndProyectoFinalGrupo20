from fastapi import HTTPException, Request
from http import HTTPStatus

from src.dtos import ResponseDto, AsociarSkillDto, GetSkillsResponseDto, SkillsDataResponseDto
from src.models import SkillCandidato, Candidato
from src.config import TECHSKILLS_SERVICE
from src.services.utils_service import get_request, validate_response


async def asociar_skill(data: AsociarSkillDto, user_id: int) -> ResponseDto:
    body: str or dict = ''
    status_code: HTTPStatus = HTTPStatus.OK

    data_keys = [key for key in data]
    skill_keys = AsociarSkillDto.get_attributes(None)
    if not all(key in data_keys for key in skill_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')
    try:
        candidato = await Candidato.findByUserId(user_id)
        skill_candidato = SkillCandidato(
            skillId=data.get('skill'), candidatoId=candidato.id, nivel_dominio=data.get('nivel_dominio')
        )
        await skill_candidato.save()

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED,
                            detail=f'{exception}')

    return ResponseDto({'detail': 'The skill was saved correctly'}, status_code)


async def skills_of_candidate(request: Request, candidate_id: int, user_id: int):
    body: str or dict = ''
    status_code: int = HTTPStatus.OK

    if not user_id:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                            detail='El usuario no tiene permisos para realizar esta acción')

    skills_candidate = await SkillCandidato.list(candidate_id)

    if not skills_candidate:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail='There are no skills associated to the selected candidate')

    skills: GetSkillsResponseDto = await get_skills(request)

    skills_response = []
    for skill_candidate in skills_candidate:
        skill_id = skill_candidate.skillId
        skill_data = next((item for item in skills if item["id"] == skill_id), None)

        skills_response.append(SkillsDataResponseDto(
            skill_id, skill_candidate.nivel_dominio, skill_data
        ))

    return ResponseDto(skills_response, status_code)


async def get_skills(request: Request):

    response_skills = await get_request(f'{TECHSKILLS_SERVICE}/skills', request)
    validate_response(response_skills.get('status_code'), response_skills.get('body'))

    return response_skills.get('body')
