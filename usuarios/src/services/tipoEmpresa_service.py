from fastapi import HTTPException
from http import HTTPStatus
from src.dtos import ResponseDto
from src.models import TipoEmpresa


async def listar_tipos_empresa() -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.CREATED

    try:
        # Realiza una consulta a la base de datos para obtener todos los tipoEmpresa
        tipoEmpresa = await TipoEmpresa.all()
        
        # Si no se encontraron tipoEmpresa, puedes devolver una lista vacía o lanzar una excepción
        if not tipoEmpresa:
            status_code=HTTPStatus.BAD_REQUEST
            body= {'detail':'No existen tipos de Empresa.'}
        else:
            # Mapea los tipoEmpresa a un formato de respuesta si es necesario
            tipoEmpresa_data = [{"id": tipoEmpresa.id, "tipoEmpresa": tipoEmpresa.tipoEmpresa} for tipoEmpresa in tipoEmpresa]
            body = tipoEmpresa_data

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))

    return ResponseDto(body, status_code)
