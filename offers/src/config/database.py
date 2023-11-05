from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from src.config import DATABASE_URL


async def connect_to_database() -> None:
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={'models': ['src.models']}
    )


def register_database(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=DATABASE_URL,
        modules={"models": ["src.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
