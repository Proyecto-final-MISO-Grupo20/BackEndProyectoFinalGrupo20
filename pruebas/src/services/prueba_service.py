from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import ResponseDto, CreatePruebaDto, PostularCandidatoDto
from src.models import Postulacion, Candidato, Prueba, Postulacion_Prueba


async def registrar_prueba(data) -> ResponseDto:
    body: str or dict = ''
    status_code: HTTPStatus = HTTPStatus.CREATED

    validate_body(data)

    try: 
        prueba = Prueba(tipo=data.get('tipo'), nombre=data.get('nombre'))
        await prueba.save()

        postulacionPrueba = Postulacion_Prueba(postulacionId=data.get('postulacionId'), pruebaId=prueba.id, calificacion=data.get('calificacion'), comentario=data.get('comentario'))
        await postulacionPrueba.save()

        body = {'detail':'Se agrego la prueba correctamente.'}

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED,
                            detail=f'{exception}')

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
        if postulacion is None:
            postulacion = await Postulacion(ofertaId=data.get('ofertaId'), candidatoId=candidato.id)
            await postulacion.save()
        else:
            status_code=HTTPStatus.BAD_REQUEST
            body= {'detail':'El candidato ya esta asociado a esta oferta'}

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED, 
                            detail=f'{exception}')

    return ResponseDto(body, status_code)

def validate_body(get_prueba_data):
    data_keys = [key for key in get_prueba_data]
    prueba_keys = CreatePruebaDto.get_attributes(None)

    if not all(key in data_keys for key in prueba_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')