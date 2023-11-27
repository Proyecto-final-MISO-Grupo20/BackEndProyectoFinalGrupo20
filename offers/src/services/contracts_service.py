from fastapi import HTTPException, Request

from src.config import CONTRACTS_SERVICE
from src.services.utils_service import get_request, validate_response


async def get_contract(request: Request, offer_id):

    response = await get_request(f'{CONTRACTS_SERVICE}/contratos/{offer_id}', request)
    body_response = response.get('body')
    validate_response(response.get('status_code'), body_response)

    return response.get('body')
