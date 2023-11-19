import os

from tortoise import Tortoise


async def init():
    await Tortoise.init(
        db_url="sqlite://test_db.sqlite",
        modules={'models': ['src.models']}
    )
    await Tortoise.generate_schemas()


async def close():
    await Tortoise.close_connections()


async def delete_test_database():
    await Tortoise.close_connections()
    os.remove("test_db.sqlite")
