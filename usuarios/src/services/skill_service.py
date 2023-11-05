from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import ResponseDto, AsociarSkillDto
from src.models import SkillCandidato, Candidato


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
        skillCandidato = SkillCandidato(skillId=data.get('skill'), candidatoId=candidato.id, nivel_dominio=data.get('nivel_dominio'))
        await skillCandidato.save()

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED, 
                            detail=f'{exception}')

    return ResponseDto(body, status_code)