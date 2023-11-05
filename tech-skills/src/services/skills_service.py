from fastapi import HTTPException, Request
from http import HTTPStatus

from src.dtos import ExceptionDto, ResponseDto, CreateSkillResponseDto, GetSkillDto
from src.models import Skills
from src.enums import TipoSkill


async def listar_skills(tipo_skill):
    body: str or dict = ''
    status_code: int = HTTPStatus.OK

    if not TipoSkill.has_value(tipo_skill):
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED,
                            detail='Invalid skill type, it must be HERRAMIENTA, HABILIDAD or IDIOMA')

    body = await Skills.list(tipo_skill)

    if not body:
        status_code = HTTPStatus.NOT_FOUND
        body = {'detail': 'There are no skills of the selected type'}

    return ResponseDto(body, status_code)


async def create_skill(data) -> ResponseDto:
    body: str or dict = ''
    status_code: HTTPStatus = HTTPStatus.CREATED

    validate_body(data)

    try:
        skill = Skills(nombre=data.get('nombre'), tipo=data.get('tipo'))

        await skill.save()

        body = CreateSkillResponseDto(skill.id, skill.nombre, skill.tipo)

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED,
                            detail=f'{exception}')

    return ResponseDto(body, status_code)


def validate_body(get_post_data):
    data_keys = [key for key in get_post_data]
    post_keys = GetSkillDto.get_attributes()

    if not all(key in data_keys for key in post_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')
