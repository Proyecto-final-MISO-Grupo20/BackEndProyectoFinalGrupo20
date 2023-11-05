from fastapi import APIRouter, Request, Response, Depends
import src.services.skills_service as skills_service
from src.authentication import get_token_header
from src.dtos import ResponseDto, GetSkillDto

router: APIRouter = APIRouter(prefix='/skills')


@router.get('/ping')
def validate_health() -> Response:
    return 'pong'


@router.post('')
async def crear_skill(request: Request, response: Response, user_id=Depends(get_token_header)) -> Response:

    data: GetSkillDto = await request.json()

    response_object: ResponseDto = await skills_service.create_skill(
        data, user_id
    )

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/herramientas')
async def listar_skills(response: Response, user_id=Depends(get_token_header)) -> Response:

    response_object: ResponseDto = await skills_service.listar_skills("HERRAMIENTA", user_id)

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/habilidades')
async def listar_skills(response: Response, user_id=Depends(get_token_header)) -> Response:

    response_object: ResponseDto = await skills_service.listar_skills("HABILIDAD", user_id)

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/idiomas')
async def listar_skills(response: Response, user_id=Depends(get_token_header)) -> Response:

    response_object: ResponseDto = await skills_service.listar_skills("IDIOMA", user_id)

    response.status_code = response_object.status_code

    return response_object.body
