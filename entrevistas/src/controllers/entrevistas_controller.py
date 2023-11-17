from fastapi import APIRouter, Request, Response, Depends
import src.services.entrevistas_service as entrevistas_service
from src.authentication import get_token_header
from src.dtos import ResponseDto, CreateEntrevistaDto, QualifyEntrevistaDto

router: APIRouter = APIRouter(prefix='/entrevistas')


@router.get('/ping')
def validate_health() -> str:
    return 'pong'


@router.post('')
async def crear_entrevista(request: Request, response: Response, user_id=Depends(get_token_header)) -> Response:

    data: CreateEntrevistaDto = await request.json()

    response_object: ResponseDto = await entrevistas_service.create_entrevista(data, user_id)

    response.status_code = response_object.status_code

    return response_object.body

@router.post('/qualify')
async def calificar_entrevista(request: Request, response: Response, user_id=Depends(get_token_header)) -> Response:

    data: QualifyEntrevistaDto = await request.json()

    response_object: ResponseDto = await entrevistas_service.qualify_entrevista(data, user_id)

    response.status_code = response_object.status_code

    return response_object.body

@router.get('')
async def listar_entrevistas_usuario(response: Response, user_id=Depends(get_token_header)) -> Response:
    response_object: ResponseDto = await entrevistas_service.list_entrevistas_by_user(user_id)
    print(response_object)
    response.status_code = response_object.status_code

    return response_object.body