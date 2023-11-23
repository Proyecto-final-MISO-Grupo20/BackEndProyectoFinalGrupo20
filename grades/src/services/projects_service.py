from fastapi import HTTPException, Request
from http import HTTPStatus

from src.config import PROJECTS_SERVICE
from src.services.utils_service import get_request, validate_response


async def validate_project(request: Request, project_id):

    project = await get_project(request, project_id)

    if not project:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN,
                            detail='The project with the given id was not found')

    return project


async def get_project(request: Request, project_id):

    get_project_response = await get_request(f'{PROJECTS_SERVICE}/proyecto/{project_id}', request)
    body_response = get_project_response.get('body')
    validate_response(get_project_response.get('status_code'), body_response)

    return get_project_response.get('body')
