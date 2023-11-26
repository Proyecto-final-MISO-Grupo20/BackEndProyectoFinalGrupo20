from fastapi import HTTPException, Request
from http import HTTPStatus

from src.config import USERS_SERVICE
from src.dtos.get_user_dto import GetUserDto
from src.services.utils_service import get_request, validate_response


async def validate_user_type(request: Request, user_id, user_type):
    if not user_id:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                            detail='Se requiere autenticación para realizar esta acción')

    user = await get_user(request, user_id)

    if (user_type == 'business' and user.get('rol') != 3) or (user_type == 'candidate' and user.get('rol') != 2):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN,
                            detail='El usuario no tiene el ROL requerido para realizar esta acción')

    return user


async def get_user(request: Request, user_id):

    get_user_response = await get_request(f'{USERS_SERVICE}/usuario/usuarios/{user_id}', request)
    user: GetUserDto = get_user_response.get('body')
    validate_response(get_user_response.get('status_code'), user)

    return user
