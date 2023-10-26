from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import ResponseDto, CreateHabilidadDto
from src.models import Habilidades, HabilidadesCandidato, Candidato


async def listar_habilidades() -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.CREATED

    try:
        # Realiza una consulta a la base de datos para obtener todos los habilidades
        habilidades = await Habilidades.all()
        
        # Si no se encontraron habilidades, puedes devolver una lista vacía o lanzar una excepción
        if not habilidades:
            status_code=HTTPStatus.BAD_REQUEST
            body= {'detail':'No existen Habilidades.'}
        else:
            # Mapea los habilidades a un formato de respuesta si es necesario
            habilidades_data = [{"id": habilidad.id, "Habilidades": habilidad.habilidad} for habilidad in habilidades]
            body = habilidades_data

    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))

    return ResponseDto(body, status_code)

async def create_habilidad(data: CreateHabilidadDto, user_id: int) -> ResponseDto:
    body: str or dict = ''
    status_code: HTTPStatus = HTTPStatus.CREATED
    try:
        candidato = await Candidato.findByUserId(user_id)
        print(candidato)
        for habilidad in data.habilidades:
            habilidadesCandidato = HabilidadesCandidato(habilidadesId=habilidad, candidatoId=candidato.id)
            await habilidadesCandidato.save()

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED, 
                            detail=f'{exception}')

    return ResponseDto(body, status_code)