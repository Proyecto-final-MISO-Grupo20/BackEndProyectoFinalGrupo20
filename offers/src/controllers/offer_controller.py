from fastapi import APIRouter, Request, Response, Depends
import src.services.offers_service as offers_service
from src.authentication import get_token_header
from src.dtos import ResponseDto, GetOfferDto

router: APIRouter = APIRouter(prefix='/offers')


@router.get('/ping')
def validate_health() -> str:
    return 'pong'


@router.post('/{project_id}')
async def crear_offer(
        request: Request, response: Response, project_id: int, user_id=Depends(get_token_header)
) -> Response:

    data: GetOfferDto = await request.json()

    response_object: ResponseDto = await offers_service.create_offer(
        data, project_id, user_id
    )

    response.status_code = response_object.status_code

    return response_object.body

@router.get('')
async def list_offer(response: Response, user_id=Depends(get_token_header)
) -> Response:

    response_object: ResponseDto = await offers_service.list_offers()

    response.status_code = response_object.status_code

    return response_object.body