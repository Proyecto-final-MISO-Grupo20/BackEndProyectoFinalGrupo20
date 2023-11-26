from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import ResponseDto
from src.models import Usuario

from src.services.utils_service import validate_user_type


async def get_user(user_id: int, logged_user_id: int):
    authenticated_user = await Usuario.get_by_id(logged_user_id)

    user = authenticated_user
    if authenticated_user.rol == 3 and user_id != logged_user_id:
        user = await Usuario.get_by_id(user_id)

        if not user:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                                detail='The user with the requested ID does not exist or there is an issue with the '
                                       'database relations')

    return ResponseDto(user, HTTPStatus.OK)


# def get_rol(user: Usuario):
#     user_type = ''
#     if user.rol == 2:
#         user_type = 'candidate'
#     elif user.rol == 3:
#         user_type = 'business'
#
#     return user_type
