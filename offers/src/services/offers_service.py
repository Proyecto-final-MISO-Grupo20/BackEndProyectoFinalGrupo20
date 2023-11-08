from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import ResponseDto, CreateOfferResponseDto, GetOfferDto, SkillsDataResponseDto
from src.models import Oferta, SkillsOferta


async def create_offer(data, project_id: int, user_id: int) -> ResponseDto:
    body: str or dict = ''
    status_code: HTTPStatus = HTTPStatus.CREATED

    validate_body(data)

    try:
        if not user_id:
            status_code = HTTPStatus.UNAUTHORIZED
            body = {'detail': 'El usuario no tiene permisos para realizar esta acción'}
        else:
            offer = Oferta(perfil=data.get('perfil'), proyecto_id=project_id, estado="DISPONIBLE")

            await offer.save()

            skills = data.get('skills')

            skills_responses = []

            for i in range(len(skills)):
                skill = skills[i]

                new_skill = SkillsOferta(
                    oferta_id=offer.id, skill_id=skill.get('skill_id'), dominio=skill.get('dominio')
                )
                await new_skill.save()

                skills_responses.append(SkillsDataResponseDto(
                    new_skill.id, new_skill.skill_id, new_skill.dominio
                ))

            body = CreateOfferResponseDto(offer.id, offer.perfil, offer.proyecto_id, offer.estado, skills_responses)

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED,
                            detail=f'{exception}')

    return ResponseDto(body, status_code)


def validate_body(get_post_data):
    data_keys = [key for key in get_post_data]
    post_keys = GetOfferDto.get_attributes()

    if not all(key in data_keys for key in post_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')

async def list_offers() -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.OK

    try:
        print('---------------------------------------')
        body = await Oferta.list("DISPONIBLE")   

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            detail=e)

    return ResponseDto(body, status_code)