import os

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///:memory')
JWT_SECRET_KEY = '7b11677e262b608e88ee6747372a1776'
