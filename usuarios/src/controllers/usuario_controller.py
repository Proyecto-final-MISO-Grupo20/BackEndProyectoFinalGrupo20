from fastapi import APIRouter, Request, Response, Depends
from typing import Union
import src.services.usuario_service as usuario_service

from src.dtos import CreateCandidatoDto, ResponseDto


router: APIRouter = APIRouter(prefix='/usuario')


@router.get('/ping')
def validate_health() -> Response:
    return 'pong'


@router.post('/candidato')
async def create_candidato(request: Request, response: Response) -> Response:
    usuario_data: CreateCandidatoDto = await request.json()
    response_object: ResponseDto = await usuario_service.create_candidato(usuario_data)

    response.status_code = response_object.status_code

    return response_object.body
