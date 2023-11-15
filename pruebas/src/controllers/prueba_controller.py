from fastapi import APIRouter, Request, Response, Depends
import src.services.prueba_service as prueba_service
from src.authentication import get_token_header
from src.dtos import ResponseDto, CreatePruebaDto, PostularCandidatoDto, GetPostulacionResponseDto

router: APIRouter = APIRouter(prefix='/pruebas')


@router.get('/ping')
def validate_health() -> str:
    return 'pong'


@router.post('')
async def registrar_prueba(request: Request, response: Response, user_id=Depends(get_token_header)) -> Response:

    data: CreatePruebaDto = await request.json()

    response_object: ResponseDto = await prueba_service.registrar_prueba(data)

    response.status_code = response_object.status_code

    return response_object.body

@router.post('/candidato')
async def create_habilidad(request: Request, response: Response, user_id=Depends(get_token_header)) -> Response:
    postulacion_data: PostularCandidatoDto = await request.json()
    response_object: ResponseDto = await prueba_service.postular_candidato(postulacion_data, user_id)

    response.status_code = response_object.status_code

    return response_object.body

@router.get('/{offer_id}/postulaciones')
async def consultar_postulaciones_oferta(response: Response, offer_id: int,  user_id=Depends(get_token_header)) -> Response:
    response_object: GetPostulacionResponseDto = await prueba_service.consultar_postulaciones_oferta(offer_id)

    response.status_code = response_object.status_code

    if response.status_code != 200:
        return response_object.body
    return response_object.postulaciones