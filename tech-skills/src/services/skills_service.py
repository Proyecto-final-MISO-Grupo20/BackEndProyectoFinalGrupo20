from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import *
from src.models import Skills
from src.enums import TipoSkill


async def listar_skills(tipo_skill):
    body: str or dict = ''
    status_code: int = HTTPStatus.OK

    if not TipoSkill.has_value(tipo_skill):
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED,
                            detail='Invalid skill type, it must be HERRAMIENTA, HABILIDAD or IDIOMA')

    try:
        body = await Skills.list(tipo_skill)

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED,
                            detail=f'{exception}')

    return ResponseDto(body, status_code)
