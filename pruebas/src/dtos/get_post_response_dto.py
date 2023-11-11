from dataclasses import dataclass
from .postulacion_dto import PostulacionDto
from http import HTTPStatus


@dataclass
class GetPostulacionResponseDto:
    postulaciones: list[PostulacionDto]
    status_code: HTTPStatus
