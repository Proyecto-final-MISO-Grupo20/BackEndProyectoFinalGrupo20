from fastapi import HTTPException, Request
import requests
from http import HTTPStatus

from src.dtos import GetGradesDto


async def get_request(path: str, request: Request):
    response = requests.get(path, headers=get_token_header(request))
    return {'body': response.json(), 'status_code': response.status_code}


def validate_response(status_code: int, response):
    if status_code != HTTPStatus.OK:
        raise HTTPException(status_code=status_code, detail=response)


def get_token_header(request: Request):
    return {'Authorization': request.headers.get('Authorization')}


def validate_body(get_post_data):
    data_keys = [key for key in get_post_data]
    post_keys = GetGradesDto.get_attributes()

    if not all(key in data_keys for key in post_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')
