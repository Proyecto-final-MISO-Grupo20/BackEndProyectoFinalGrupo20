from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import CreateCandidatoDto, ResponseDto, CreateCandidatoResponseDto, CreateEmpresaDto, PostularCandidatoDto
from src.models import Candidato, Usuario, Postulacion, Empresa, Ubicacion
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
        # Llama al método get_by_username para buscar el usuario por nombre de usuario
        user = await Usuario.get_by_username(username=data.get('username'))
        
        if user:
            status_code=HTTPStatus.BAD_REQUEST
            body= {'detail':'El username ya esta relacionado a un usuario.'}
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
        print(e)
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='El username ya esta relacionado a un usuario.')

    return ResponseDto(body, status_code)

async def create_empresa(data: CreateEmpresaDto) -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.CREATED

    data_keys = [key for key in data]
    

    empresa_keys = CreateEmpresaDto.get_attributes(None)

    if not all(key in data_keys for key in empresa_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')

    try:
        # Llama al método get_by_username para buscar el usuario por nombre de usuario
        user = await Usuario.get_by_username(username=data.get('username'))
        
        if user:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='El username ya esta relacionado a un usuario.')
        else:
            encrypted_password = generate_password_hash(data.get('password'))
            usuario = Usuario(nombre=data.get('nombre'),
                          tipo_documento=data.get('tipo_documento'), documento=data.get('documento'),
                          username=data.get('username'), password=encrypted_password, 
                          email=data.get('email'), rol=3)
            await usuario.save()
            empresa = Empresa(tipoEmpresaID=data.get('tipoEmpresaId'), segmentoID=data.get('segmentoId'),
                            usuarioId=usuario.id)
            await empresa.save()    
            ubicacion = Ubicacion(direccion=data.get('direccion'), pais=data.get('pais'), ciudad=data.get('ciudad'), empresaId=empresa.id)
            await ubicacion.save()

            body = CreateCandidatoResponseDto(usuario.username)
            

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='El username ya esta relacionado a un usuario.')

    return ResponseDto(body, status_code)

async def postular_candidato(data: PostularCandidatoDto, user_id: int) -> ResponseDto:
    body: str or dict = ''
    status_code: HTTPStatus = HTTPStatus.OK

    data_keys = [key for key in data]
    postulacion_keys = PostularCandidatoDto.get_attributes(None)
    if not all(key in data_keys for key in postulacion_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')
    try:
        candidato = await Candidato.findByUserId(user_id)
        postulacion = await Postulacion.getPostulacion(candidato.id, data.get('ofertaId'))
        print(postulacion)
        if postulacion is None:
            postulacion = await Postulacion(ofertaId=data.get('ofertaId'), candidatoId=candidato.id)
            await postulacion.save()
        else:
            status_code=HTTPStatus.BAD_REQUEST
            body= {'detail':'El candidato ya esta asociado a esta oferta'}

    except Exception as exception:
        print(exception)
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED, 
                            detail=f'{exception}')

    return ResponseDto(body, status_code)