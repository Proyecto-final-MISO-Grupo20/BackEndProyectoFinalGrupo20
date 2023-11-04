from fastapi import APIRouter, Request, Response, Depends
import src.services.skills_service as skills_service

from src.dtos import ResponseDto, CreateSkillDto

router: APIRouter = APIRouter(prefix='/skills')


@router.get('/ping')
def validate_health() -> Response:
    return 'pong'


@router.get('/herramientas')
async def listar_skills() -> Response:

    response_object: ResponseDto = await skills_service.listar_skills("HERRAMIENTA")

    return response_object.body


@router.get('/habilidades')
async def listar_skills() -> Response:

    response_object: ResponseDto = await skills_service.listar_skills("HABILIDAD")

    return response_object.body


@router.get('/idiomas')
async def listar_skills() -> Response:

    response_object: ResponseDto = await skills_service.listar_skills("IDIOMA")

    return response_object.body

