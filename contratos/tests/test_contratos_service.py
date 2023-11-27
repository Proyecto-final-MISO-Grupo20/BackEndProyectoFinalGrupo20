import pytest
from fastapi import HTTPException
from httpx import request
from .db_tests import init, close
from http import HTTPStatus
from src.services import contrato_service


@pytest.mark.asyncio
async def test_registrar_contrato_ok():
    await init()

    with pytest.raises(HTTPException) as exc_info:
        await contrato_service.registrar_contrato_candidato(request, {"fecha_inicio": 20230601,
                                                           "meses": 12,
                                                           "valor": 25000000,
                                                            "candidato_id": 1
                                                           }, 1)

    assert exc_info.value.status_code == HTTPStatus.PRECONDITION_FAILED

    await close() 

@pytest.mark.asyncio
async def test_obtener_candidato():
    await init()

    test_response = await contrato_service.obtener_candidato(1)

    assert test_response.status_code == 200

    await close() 
