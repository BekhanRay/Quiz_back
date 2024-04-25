from decouple import config

PRODUCTION = config('PRODUCTION', cast=bool)
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')

POSTGRES_DB = config('POSTGRES_DB')
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_HOST = config('POSTGRES_HOST')
POSTGRES_PORT = config('POSTGRES_PORT', cast=int)