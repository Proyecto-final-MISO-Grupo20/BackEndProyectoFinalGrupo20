from fastapi import HTTPException
from http import HTTPStatus
from src.dtos import ResponseDto, CreateContratoDto
from src.models import ContratoCandidato
from datetime import datetime
from dateutil.relativedelta import relativedelta


async def registrar_contrato_candidato(data, offer_id) -> ResponseDto:
    body: str or dict = ''
    status_code: HTTPStatus = HTTPStatus.CREATED

    validate_body(data)
    fecha_inicio_str = str(data.get('fecha_inicio'))
    fechaInicial = datetime.strptime(fecha_inicio_str, '%Y%m%d')
    meses = data.get('meses')
    fechaFinal = fechaInicial + relativedelta(months=meses)

    try: 
        contratoCandidato = ContratoCandidato(fecha_inicio=fechaInicial, fecha_fin=fechaFinal, valor=data.get('valor'), ofertaId = offer_id)
        await contratoCandidato.save()

        body = {'detail':'Se creo el contrato correctamente.'}

    except Exception as exception:
        raise HTTPException(status_code=HTTPStatus.PRECONDITION_FAILED,
                            detail=f'{exception}')

    return ResponseDto(body, status_code)

    

def validate_body(get_contrato_data):
    data_keys = [key for key in get_contrato_data]
    contrato_keys = CreateContratoDto.get_attributes(None)

    if not all(key in data_keys for key in contrato_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')