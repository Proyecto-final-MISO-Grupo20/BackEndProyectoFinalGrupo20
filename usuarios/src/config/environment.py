import os

DATABASE_URL: str = os.environ.get('DATABASE_URL')
AUTH_SERVICE: str = f"http://{os.getenv('USERS_PATH')}"
