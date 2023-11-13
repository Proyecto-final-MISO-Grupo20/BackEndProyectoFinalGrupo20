from fastapi import HTTPException, Request
from http import HTTPStatus

from src.dtos import ResponseDto, AsociarSkillDto, GetSkillsResponseDto, SkillsDataResponseDto
from src.models import SkillCandidato, Candidato, Empresa, Usuario
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
        candidato = await Candidato.find_by_user_id(user_id)
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

    await validate_user_type(user_id, 'business')

    skills_response = await candidate_skills(candidate_id, request)

    return ResponseDto(skills_response, status_code)


async def skills_of_authenticated(request: Request, user_id: int):
    body: str or dict = ''
    status_code: int = HTTPStatus.OK

    candidate = await validate_user_type(user_id, 'candidate')

    skills_response = await candidate_skills(candidate.id, request)

    return ResponseDto(skills_response, status_code)


async def candidate_skills(candidate_id, request):
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
    return skills_response


async def get_skills(request: Request):

    response_skills = await get_request(f'{TECHSKILLS_SERVICE}/skills', request)
    validate_response(response_skills.get('status_code'), response_skills.get('body'))

    return response_skills.get('body')


async def validate_user_type(user_id, type):
    if not user_id:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                            detail='Se requiere autenticación para realizar esta acción')
    user: Usuario = None
    if type == 'business':
        user = await Empresa.find_by_user_id(user_id)
    elif type == 'candidate':
        user = await Candidato.find_by_user_id(user_id)

    if not user:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN,
                            detail='El usuario no tiene el ROL requerido para realizar esta acción')
    return user
