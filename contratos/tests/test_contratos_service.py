import pytest
from fastapi import HTTPException

from .db_tests import init, close
from http import HTTPStatus
from src.services import contrato_service


@pytest.mark.asyncio
async def test_registrar_contrato_ok():
    await init()

    test_response = await contrato_service.registrar_contrato_candidato({"fecha_inicio": 20230601,
                                                           "meses": 12,
                                                           "valor": 25000000
                                                           }, 1)

    assert test_response.status_code == 201

    await close() 
