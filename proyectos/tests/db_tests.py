from tortoise import Tortoise
from src.models import Empresa


async def init():
    await Tortoise.init(
        db_url="sqlite://test_db.sqlite",
        modules={'models': ['src.models']}
    )
    await Tortoise.generate_schemas()

    empresa = Empresa(tipoEmpresaID=1, segmentoID=1,
                            usuarioId=1)

    await empresa.save()  


async def close():
    await Tortoise.close_connections()
