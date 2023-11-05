from fastapi import APIRouter, Request, Response, Depends
import src.services.skills_service as skills_service

from src.dtos import ResponseDto, GetSkillDto

router: APIRouter = APIRouter(prefix='/skills')


@router.get('/ping')
def validate_health() -> Response:
    return 'pong'


@router.post('')
async def crear_skill(request: Request, response: Response) -> Response:

    data: GetSkillDto = await request.json()

    response_object: ResponseDto = await skills_service.create_skill(
        data
    )

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/herramientas')
async def listar_skills(response: Response) -> Response:

    response_object: ResponseDto = await skills_service.listar_skills("HERRAMIENTA")

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/habilidades')
async def listar_skills(response: Response) -> Response:

    response_object: ResponseDto = await skills_service.listar_skills("HABILIDAD")

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/idiomas')
async def listar_skills(response: Response) -> Response:

    response_object: ResponseDto = await skills_service.listar_skills("IDIOMA")

    response.status_code = response_object.status_code

    return response_object.body

