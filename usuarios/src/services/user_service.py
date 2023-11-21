from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import ResponseDto
from src.models import Usuario

from src.services.utils_service import validate_user_type


async def get_user(user_id: int, logged_user_id: str):
    await validate_user_type(logged_user_id, 'business')

    user = await Usuario.get_by_id(user_id)

    if not user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail='The user with the requested ID does not exist or there is an issue with the '
                                   'database relations')

    return ResponseDto(user, HTTPStatus.OK)
