from fastapi import APIRouter, Request, Response, Depends
from typing import Union
import src.services.proyecto_service as proyecto_service
import src.services.empleado_service as empleado_service
from src.authentication import get_token_header
from src.dtos import CreateProyectoDto, CreateEmpleadoDto, ResponseDto


router: APIRouter = APIRouter(prefix='/proyecto')


@router.get('/ping')
def validate_health() -> Response:
    return 'pong'

@router.post('')
async def create_proyecto(request: Request, response: Response, user_id=Depends(get_token_header)) -> Response:
    proyecto_data: CreateProyectoDto = await request.json()
    response_object: ResponseDto = await proyecto_service.create_proyecto(proyecto_data, user_id)

    response.status_code = response_object.status_code

    return response_object.body

@router.post('/empleado')
async def create_empleado(request: Request, response: Response, user_id=Depends(get_token_header)) -> Response:
    empleado_data: CreateEmpleadoDto = await request.json()
    response_object: ResponseDto = await empleado_service.create_empleado(empleado_data, user_id)

    response.status_code = response_object.status_code

    return response_object.body


@router.get('')
async def listar_proyectos(response: Response, user_id=Depends(get_token_header)) -> Response:
    response_object: ResponseDto = await proyecto_service.list_proyectos(user_id)

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/{project_id}')
async def get_project(response: Response, project_id, user_id=Depends(get_token_header)) -> Response:
    response_object: ResponseDto = await proyecto_service.get_project(project_id, user_id)

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/empleados/list')
async def listar_empleados(response: Response, user_id=Depends(get_token_header)) -> Response:
    response_object: ResponseDto = await empleado_service.list_empleados(user_id)

    response.status_code = response_object.status_code

    return response_object.body