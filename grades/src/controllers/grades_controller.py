from fastapi import APIRouter, Request, Response, Depends
from src.authentication import get_token_header
from src.dtos import ResponseDto
from src.services import grades_service

router: APIRouter = APIRouter(prefix='/grades')


@router.get('/ping')
def validate_health() -> Response:
    return 'pong'


@router.post('/candidates/{candidate_id}/projects/{project_id}')
async def create_grades(request: Request, response: Response, candidate_id: int, project_id: int, user_id=Depends(get_token_header)) -> Response:
    response_object: ResponseDto = await grades_service.create_grades(request, candidate_id, project_id, user_id)
    response.status_code = response_object.status_code

    return response_object.body
