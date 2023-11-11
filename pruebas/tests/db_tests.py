from tortoise import Tortoise
from src.models import Candidato, Usuario


async def init():
    await Tortoise.init(
        db_url="sqlite://test_db.sqlite",
        modules={'models': ['src.models']}
    )
    await Tortoise.generate_schemas()

    candidato = Candidato(fecha_nacimiento=19990101, telefono=123,
                            pais="Colombia", ciudad="Bogota", usuarioId=1)

    await candidato.save() 

    usuario = Usuario(nombre="Usuario Prueba", tipo_documento=123,
                            documento="123", username="userPrueba",
                            password="123", email="prueba@gmail.com", rol=1)

    await usuario.save() 


async def close():
    await Tortoise.close_connections()
