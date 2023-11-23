from fastapi import HTTPException, Request
import requests
from http import HTTPStatus

from src.models import Usuario, Empresa, Candidato


async def get_request(path: str, request: Request):
    response = requests.get(path, headers=get_token_header(request))
    return {'body': response.json(), 'status_code': response.status_code}


def validate_response(status_code: int, response):
    if status_code != HTTPStatus.OK:
        raise HTTPException(status_code=status_code, detail=response)


def get_token_header(request: Request):
    return {'Authorization': request.headers.get('Authorization')}


async def validate_user_type(user_id, user_type):
    if not user_id:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                            detail='Se requiere autenticación para realizar esta acción')
    user = None
    if user_type == 'business':
        user = await Empresa.find_by_user_id(user_id)
    elif user_type == 'candidate':
        user = await Candidato.find_by_user_id(user_id)

    if user is None:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN,
                            detail='El usuario no tiene el ROL requerido para realizar esta acción')
    return user
