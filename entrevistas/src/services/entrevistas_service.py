from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import ResponseDto, CreateEntrevistaDto, QualifyEntrevistaDto
from src.models import Entrevista, EntrevistaUsuario
from tortoise.exceptions import DoesNotExist


async def create_entrevista(data, user_id: int) -> ResponseDto:
    body: str or dict = ''
    status_code: HTTPStatus = HTTPStatus.CREATED
    post_keys = CreateEntrevistaDto.get_attributes()

    ##Valida que la petición contenga la info necesaria 
    validate_body(data, post_keys)

    try:
        if not user_id:
            status_code = HTTPStatus.UNAUTHORIZED
            body = {'detail': 'El usuario no tiene permisos para realizar esta acción'}
        else:

            #Crea la entrevista
            entrevista = Entrevista(titulo=data.get('titulo'), fecha=data.get('fecha'), calificacion = 0, comentario = "")
            await entrevista.save()

            #Añade empresa que agenda la entrevista
            nuevo_usuario = EntrevistaUsuario(usuarioId=user_id, entrevistaId = entrevista.id)
            await nuevo_usuario.save()

            #Añade el listado de otros participantes 
            usuarios = data.get('usuarios')
            for i in range(len(usuarios)):

                usuario = usuarios[i]
                nuevo_usuario = EntrevistaUsuario(usuarioId=usuario, entrevistaId = entrevista.id)
                await nuevo_usuario.save()
            
    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED,
                            detail=f'{exception}')

    return ResponseDto(body, status_code)

async def qualify_entrevista(data, user_id: int) -> ResponseDto:
    body: str or dict = ''
    status_code: HTTPStatus = HTTPStatus.OK
    post_keys = QualifyEntrevistaDto.get_attributes()

    ##Valida que la petición contenga la info necesaria 
    validate_body(data, post_keys)

    try:
        if not user_id:
            status_code = HTTPStatus.UNAUTHORIZED
            body = {'detail': 'El usuario no tiene permisos para realizar esta acción'}
        else:
            
            #Actualiza la entrevista
            try:
                entrevista = await Entrevista.get(id=data.get('id'))
                entrevista.calificacion = data.get('calificacion')
                entrevista.comentario = data.get('comentario')
                await entrevista.save()

                body = entrevista
            except DoesNotExist:
                # Manejar el caso donde no se encuentra la entrevista
                status_code = HTTPStatus.NOT_FOUND
                body = {'detail': 'La entrevista no existe'}
            
    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED,
                            detail=f'{exception}')

    return ResponseDto(body, status_code)


    

async def list_entrevistas_by_user(user_id: int) -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.OK

    try:

        entrevistas = []
        try:
            #Lista todas las entrevistas de un usuario
            entrevistasUsuario = await EntrevistaUsuario.listByUser(user_id)
            for entrevistaUsuario in entrevistasUsuario:
                entrevista = await Entrevista.get(id = entrevistaUsuario.entrevistaId) 
                entrevistas.append(entrevista)

            #Si no hay ofertas relacionadas
            if len(entrevistas) == 0:
                return ResponseDto({'detail': 'No hay entrevistas para este usuario.'}, HTTPStatus.NOT_FOUND)
        except DoesNotExist:
                # Manejar el caso donde no se encuentra la entrevista
                return ResponseDto({'detail': 'No hay entrevistas para este usuario.'}, HTTPStatus.NOT_FOUND)
        
        return ResponseDto(entrevistas, status_code)

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            detail=e)


def validate_body(get_post_data, post_keys):
    data_keys = [key for key in get_post_data]

    if not all(key in data_keys for key in post_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')