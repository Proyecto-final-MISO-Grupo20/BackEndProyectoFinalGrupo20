from tortoise import Tortoise, run_async
from src.config import connect_to_database


async def create_schema():
    await connect_to_database()
    await Tortoise.generate_schemas()


if __name__ == '__main__':
    run_async(create_schema())
