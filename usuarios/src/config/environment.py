import os

DATABASE_URL: str = os.getenv('DATABASE_URL').replace('postgresql', 'postgres')
AUTH_SERVICE: str = f"http://{os.getenv('USERS_PATH')}"
