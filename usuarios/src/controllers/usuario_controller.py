from fastapi import APIRouter, Request, Response, Depends
from typing import Union
import src.services.usuario_service as usuario_service
import src.services.segmento_service as segmento_service
import src.services.tipoEmpresa_service as tipo_empresa_service

from src.dtos import CreateCandidatoDto, ResponseDto, CreateEmpresaDto


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

@router.post('/empresa')
async def create_candidato(request: Request, response: Response) -> Response:
    print(request.json())
    empresa_data: CreateEmpresaDto = await request.json()
    response_object: ResponseDto = await usuario_service.create_empresa(empresa_data)

    response.status_code = response_object.status_code

    return response_object.body

@router.get('/segmentos')
async def create_candidato(response: Response) -> Response:
    response_object: ResponseDto = await segmento_service.listar_segmentos()

    response.status_code = response_object.status_code

    return response_object.body

@router.get('/tipoEmpresa')
async def create_candidato(response: Response) -> Response:
    response_object: ResponseDto = await tipo_empresa_service.listar_tipos_empresa()

    response.status_code = response_object.status_code

    return response_object.body