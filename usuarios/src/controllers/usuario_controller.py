from fastapi import APIRouter, Request, Response, Depends
import src.services.business_service as business_service
import src.services.candidate_service as candidate_service
import src.services.segmento_service as segmento_service
import src.services.skills_service as skills_service
from src.authentication import get_token_header

from src.dtos import CreateCandidatoDto, ResponseDto, CreateEmpresaDto, AsociarSkillDto

router: APIRouter = APIRouter(prefix='/usuario')


@router.get('/ping')
def validate_health() -> str:
    return 'pong'


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


@router.get('/segmentos')
async def listar_segmentos(response: Response) -> Response:
    response_object: ResponseDto = await segmento_service.listar_segmentos()

    response.status_code = response_object.status_code

    return response_object.body


@router.get('/tipoEmpresa')
async def create_candidato(response: Response) -> Response:
    response_object: ResponseDto = await business_service.listar_tipos_empresa()

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
