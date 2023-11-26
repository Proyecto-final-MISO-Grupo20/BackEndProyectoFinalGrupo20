from fastapi import HTTPException, Request
from http import HTTPStatus

from src.services.grades_service import candidate_grades, grades_of_candidate
from src.services.skills_service import candidate_skills
from src.dtos import CreateCandidatoDto, ResponseDto, CreateCandidatoResponseDto, GetCandidatesDto
from src.models import Candidato, Usuario
from werkzeug.security import generate_password_hash

from src.services.utils_service import validate_user_type


async def create_candidato(data: CreateCandidatoDto) -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.CREATED

    data_keys = [key for key in data]
    candidato_keys = CreateCandidatoDto.get_attributes(None)

    if not all(key in data_keys for key in candidato_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')
    try:
        # Llama al método get_by_username para buscar el usuario por nombre de usuario
        user = await Usuario.get_by_username(username=data.get('username'))

        if user:
            status_code = HTTPStatus.BAD_REQUEST
            body = {'detail': 'El username ya esta relacionado a un usuario.'}
        else:

            encrypted_password = generate_password_hash(data.get('password'))

            usuario = Usuario(nombre=data.get('nombre'),
                              tipo_documento=data.get('tipo_documento'), documento=data.get('documento'),
                              username=data.get('username'), password=encrypted_password,
                              email=data.get('email'), rol=2)

            await usuario.save()

            candidato = Candidato(fecha_nacimiento=data.get('fecha_nacimiento'), telefono=data.get('telefono'),
                                  pais=data.get('pais'), ciudad=data.get('ciudad'),
                                  usuarioId=usuario.id)

            await candidato.save()

            body = CreateCandidatoResponseDto(usuario.username)

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))

    return ResponseDto(body, status_code)


async def get_candidates(request: Request, user_id: int):
    await validate_user_type(user_id, 'business')
    candidates_list = await Candidato.list()

    if not candidates_list:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail='There are currently no registered candidates')

    candidates_response = []
    for candidate in candidates_list:
        candidate_user_id = candidate.usuarioId

        user = await Usuario.get_by_id(candidate_user_id)

        if not user:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                                detail='The user with the requested ID does not exist or there is an issue with the '
                                       'database relations')

        candidate_skills_response = await candidate_skills(candidate.id, request)

        candidate_grades_response = await grades_of_candidate(request, candidate.id, user_id)

        candidate_data = GetCandidatesDto(
            candidate.id, candidate.usuarioId, candidate.fecha_nacimiento, candidate.telefono, candidate.pais,
            candidate.ciudad, user.nombre, user.tipo_documento, user.documento, user.email,
            candidate_skills_response,
            candidate_grades_response
        )

        candidates_response.append(candidate_data)

    return ResponseDto(candidates_response, HTTPStatus.OK)
