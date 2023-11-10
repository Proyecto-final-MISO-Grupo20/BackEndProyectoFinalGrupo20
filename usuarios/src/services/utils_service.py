from fastapi import HTTPException, Request
import requests
from http import HTTPStatus


async def get_request(path: str, request: Request):
    response = requests.get(path, headers=get_token_header(request))
    return {'body': response.json(), 'status_code': response.status_code}


def validate_response(status_code: int, response):
    if status_code != HTTPStatus.OK:
        raise HTTPException(status_code=status_code, detail=response)


def get_token_header(request: Request):
    return {'Authorization': request.headers.get('Authorization')}
