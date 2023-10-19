from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import CreateCandidatoDto, ResponseDto, CreateCandidatoResponseDto
from src.models import Candidato, Usuario
from werkzeug.security import generate_password_hash


async def create_candidato(data: CreateCandidatoDto) -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.CREATED

    data_keys = [key for key in data]
    candidato_keys = CreateCandidatoDto.get_attributes(None)

    if not all(key in data_keys for key in candidato_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')

    try:
        print('---------------------------------------------------')
        print(data.get('username'))
        # Llama al método get_by_username para buscar el usuario por nombre de usuario
        user = await Usuario.get_by_username(username=data.get('username'))
        
        if user:
            print(user)
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='El username ya esta relacionado a un usuario.')
        else:

            encrypted_password = generate_password_hash(data.get('password'))

            usuario = Usuario(nombre=data.get('nombre'),
                          tipo_documento=data.get('tipo_documento'), documento=data.get('documento'),
                          username=data.get('username'), password=encrypted_password, 
                          email=data.get('email'), rol=3)

            await usuario.save()

            candidato = Candidato(fecha_nacimiento=data.get('fecha_nacimiento'), telefono=data.get('telefono'),
                            pais=data.get('pais'), ciudad=data.get('ciudad'),
                            usuarioId=usuario.id)

            await candidato.save()    

            body = CreateCandidatoResponseDto(usuario.username)
            

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='El username ya esta relacionado a un usuario.')

    return ResponseDto(body, status_code)
