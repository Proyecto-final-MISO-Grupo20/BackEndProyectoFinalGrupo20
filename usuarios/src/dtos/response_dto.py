from dataclasses import dataclass
from http import HTTPStatus

@dataclass
class ResponseDto:
    body: str or dict
    status_code: HTTPStatus
    