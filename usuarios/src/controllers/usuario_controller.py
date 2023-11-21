from fastapi import APIRouter, Request, Response, Depends
from src.services import user_service, skills_service, candidate_service, business_service
from src.authentication import get_token_header

from src.dtos import CreateCandidatoDto, ResponseDto, CreateEmpresaDto, AsociarSkillDto

router: APIRouter = APIRouter(prefix='/usuario')


@router.get('/ping')
def validate_health() -> str:
    return 'pong'


@router.get('/{user_id}')
async def get_user(response: Response, user_id: int, logged_user_id=Depends(get_token_header)) -> Response:
    response_object: ResponseDto = await user_service.get_user(user_id, logged_user_id)
    response.status_code = response_object.status_code

    return response_object.body


@router.post('/candidato')
async def create_candidate(request: Request, response: Response) -> Response:
    usuario_data: CreateCandidatoDto = await request.json()
    response_object: ResponseDto = await candidate_service.create_candidato(usuario_data)

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/candidatos')
async def get_candidates(request: Request, response: Response, user_id=Depends(get_token_header)) -> Response:

    response_object: ResponseDto = await candidate_service.get_candidates(request, user_id)

    response.status_code = response_object.status_code

    return response_object.body

@router.post('/empresa')
async def create_business(request: Request, response: Response) -> Response:
    empresa_data: CreateEmpresaDto = await request.json()
    response_object: ResponseDto = await business_service.create_empresa(empresa_data)

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/empresa/segmentos')
async def get_business_segments(response: Response) -> Response:
    response_object: ResponseDto = await business_service.get_business_segments()

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/empresa/tipos')
async def get_business_types(response: Response) -> Response:
    response_object: ResponseDto = await business_service.get_business_types()

    response.status_code = response_object.status_code

    return response_object.body


@router.post('/skills')
async def add_skill_to_candidate(request: Request, response: Response, user_id=Depends(get_token_header)) -> Response:
    skills_data: AsociarSkillDto = await request.json()
    response_object: ResponseDto = await skills_service.asociar_skill(skills_data, user_id)

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/skills/{candidate_id}')
async def skills_of_candidate(request: Request, response: Response, candidate_id,
                              user_id=Depends(get_token_header)) -> Response:
    response_object: ResponseDto = await skills_service.skills_of_candidate(request, candidate_id, user_id)

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/skills')
async def skills_of_candidate(request: Request, response: Response, user_id=Depends(get_token_header)) -> Response:
    response_object: ResponseDto = await skills_service.skills_of_authenticated(request, user_id)

    response.status_code = response_object.status_code

    return response_object.body
