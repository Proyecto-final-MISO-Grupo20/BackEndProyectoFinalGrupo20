from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import ResponseDto, CreateCandidatoResponseDto, CreateEmpresaDto
from src.models import Usuario, Empresa, Ubicacion, TipoEmpresa
from werkzeug.security import generate_password_hash

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


async def listar_tipos_empresa() -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.CREATED

    try:
        # Realiza una consulta a la base de datos para obtener todos los tipoEmpresa
        tipoEmpresa = await TipoEmpresa.all()

        # Si no se encontraron tipoEmpresa, puedes devolver una lista vacía o lanzar una excepción
        if not tipoEmpresa:
            status_code = HTTPStatus.BAD_REQUEST
            body = {'detail': 'No existen tipos de Empresa.'}
        else:
            # Mapea los tipoEmpresa a un formato de respuesta si es necesario
            tipoEmpresa_data = tipoEmpresa_data = [{"id": tipoEmpresa.id, "tipo": tipoEmpresa.tipo} for tipoEmpresa in
                                                   tipoEmpresa]
            body = tipoEmpresa_data

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))

    return ResponseDto(body, status_code)

