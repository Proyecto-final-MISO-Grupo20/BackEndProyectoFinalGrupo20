import requests

from fastapi import HTTPException, Header, Request
from http import HTTPStatus
from functools import wraps

from src.config import AUTH_SERVICE


def get_token_header(request: Request):
    request_headers = {'Authorization': request.headers.get('Authorization')}
    response = requests.get(f'{AUTH_SERVICE}/auth/me', headers=request_headers)
    response_json = response.json()

    if response.status_code != HTTPStatus.OK:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail=response_json)

    return response_json.get('id')
