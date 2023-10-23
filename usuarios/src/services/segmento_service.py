from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import ResponseDto
from src.models import Segmento


async def listar_segmentos() -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.CREATED

    try:
        # Realiza una consulta a la base de datos para obtener todos los segmentos
        segmentos = await Segmento.all()
        
        # Si no se encontraron segmentos, puedes devolver una lista vacía o lanzar una excepción
        if not segmentos:
            status_code=HTTPStatus.BAD_REQUEST
            body= {'detail':'No existen segmentos.'}
        else:
            # Mapea los segmentos a un formato de respuesta si es necesario
            segmentos_data = [{"id": segmento.id, "segmento": segmento.segmento} for segmento in segmentos]
            body = segmentos_data

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))

    return ResponseDto(body, status_code)
