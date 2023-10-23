import pytest

from .db_tests import init, close
from http import HTTPStatus
from src.services import segmento_service
from fastapi.exceptions import HTTPException
from src.models import Segmento




@pytest.mark.asyncio
async def test_listar_vacio():
    await init()
    test_response = await segmento_service.listar_segmentos()
    
    assert test_response.status_code == HTTPStatus.BAD_REQUEST

    await close()

@pytest.mark.asyncio
async def test_listar():
    await init()
    segmento = Segmento(segmento = 'prueba')
    await segmento.save()
    test_response = await segmento_service.listar_segmentos()
    
    assert test_response.status_code == HTTPStatus.CREATED

    await close()



