import pytest

from src.models import TipoEmpresa, Segmento
from src.services import business_service
from .db_tests import init, close
from http import HTTPStatus


@pytest.mark.asyncio
async def test_not_found_business_types():
    await init()
    test_response = await business_service.get_business_types()

    assert test_response.status_code == HTTPStatus.NOT_FOUND

    await close()


@pytest.mark.asyncio
async def test_get_business_types():
    await init()
    segmento = TipoEmpresa(tipo='Privada')
    await segmento.save()
    test_response = await business_service.get_business_types()

    assert test_response.status_code == HTTPStatus.OK

    await close()


@pytest.mark.asyncio
async def test_not_found_segments():
    await init()
    test_response = await business_service.get_business_segments()

    assert test_response.status_code == HTTPStatus.NOT_FOUND

    await close()


@pytest.mark.asyncio
async def test_get_segments():
    await init()
    segmento = Segmento(segmento='prueba')
    await segmento.save()
    test_response = await business_service.get_business_segments()

    assert test_response.status_code == HTTPStatus.OK

    await close()
