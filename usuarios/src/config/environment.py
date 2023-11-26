import os

DATABASE_URL: str = os.environ.get('DATABASE_URL')
AUTH_SERVICE: str = f"http://{os.getenv('AUTH_PATH')}"
TECHSKILLS_SERVICE: str = f"http://{os.getenv('TECHSKILLS_PATH')}"
GRADES_SERVICE: str = f"http://{os.getenv('GRADES_PATH')}"
