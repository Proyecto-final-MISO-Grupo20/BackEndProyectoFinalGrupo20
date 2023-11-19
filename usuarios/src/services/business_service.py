from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import ResponseDto, CreateCandidatoResponseDto, CreateEmpresaDto
from src.models import Usuario, Empresa, Ubicacion, TipoEmpresa, Segmento
from werkzeug.security import generate_password_hash


async def create_empresa(data: CreateEmpresaDto) -> ResponseDto:
    body: str or dict = ''
    status_code = HTTPStatus.CREATED

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
            ubicacion = Ubicacion(direccion=data.get('direccion'), pais=data.get('pais'), ciudad=data.get('ciudad'),
                                  empresaId=empresa.id)
            await ubicacion.save()

            body = CreateCandidatoResponseDto(usuario.username)

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='El username ya esta relacionado a un usuario.')

    return ResponseDto(body, status_code)


async def get_business_types() -> ResponseDto:
    status_code = HTTPStatus.OK

    tipo_empresa = await TipoEmpresa.all()

    if not tipo_empresa:
        status_code = HTTPStatus.NOT_FOUND
        body = {'detail': 'No existen tipos de Empresa.'}
    else:
        body = [{"id": tipoEmpresa.id, "tipo": tipoEmpresa.tipo} for tipoEmpresa in tipo_empresa]

    return ResponseDto(body, status_code)


async def get_business_segments() -> ResponseDto:
    status_code = HTTPStatus.OK

    segmentos = await Segmento.all()

    if not segmentos:
        status_code = HTTPStatus.NOT_FOUND
        body = {'detail': 'No existen segmentos.'}
    else:
        segmentos_data = [{"id": segmento.id, "segmento": segmento.segmento} for segmento in segmentos]
        body = segmentos_data

    return ResponseDto(body, status_code)
