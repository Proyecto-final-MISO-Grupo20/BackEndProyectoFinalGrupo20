import os

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///:memory')
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

