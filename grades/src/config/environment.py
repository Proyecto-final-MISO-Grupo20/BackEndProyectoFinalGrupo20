import os

DATABASE_URL: str = os.environ.get('DATABASE_URL')
AUTH_SERVICE: str = f"http://{os.getenv('AUTH_PATH')}"
USERS_SERVICE: str = f"http://{os.getenv('USERS_PATH')}"
PROJECTS_SERVICE: str = f"http://{os.getenv('PROJECTS_PATH')}"
