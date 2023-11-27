from fastapi import APIRouter, Request, Response, Depends
import src.services.contrato_service as contrato_service
from src.authentication import get_token_header
from src.dtos import ResponseDto, CreateContratoDto

router: APIRouter = APIRouter(prefix='/contratos')


@router.get('/ping')
def validate_health() -> str:
    return 'pong'


@router.post('/{oferta_id}')
async def registrar_contrato_candidato(request: Request, response: Response, oferta_id, user_id=Depends(get_token_header)) -> Response:

    data: CreateContratoDto = await request.json()

    response_object: ResponseDto = await contrato_service.registrar_contrato_candidato(request, data, oferta_id)

    response.status_code = response_object.status_code

    return response_object.body

@router.get('/{oferta_id}')
async def obtener_candidato(response: Response, oferta_id) -> Response:


    response_object: ResponseDto = await contrato_service.obtener_candidato(oferta_id)

    response.status_code = response_object.status_code

    return response_object.body
