from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import ResponseDto, CreateHerramientaDto
from src.models import Herramientas, Candidato, HerramientasCandidato


async def listar_herramientas() -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.CREATED

    try:
        # Realiza una consulta a la base de datos para obtener todos los segmentos
        herramientas = await Herramientas.all()
        
        # Si no se encontraron segmentos, puedes devolver una lista vacía o lanzar una excepción
        if not herramientas:
            status_code=HTTPStatus.BAD_REQUEST
            body= {'detail':'No existen herramientas.'}
        else:
            # Mapea los segmentos a un formato de respuesta si es necesario
            herramientas_data = [{"id": herramienta.id, "herramientas": herramienta.herramienta} for herramienta in herramientas]
            body = herramientas_data

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))

    return ResponseDto(body, status_code)

async def create_herramienta(data: CreateHerramientaDto, user_id: int) -> ResponseDto:
    body: str or dict = ''
    status_code: HTTPStatus = HTTPStatus.CREATED
    try:
        candidato = await Candidato.findByUserId(user_id)
        print(candidato)
        for herramienta in data.herramientas:
            herramientasCandidato = HerramientasCandidato(herramientasId=herramienta, candidatoId=candidato.id)
            await herramientasCandidato.save()

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED, 
                            detail=f'{exception}')

    return ResponseDto(body, status_code)