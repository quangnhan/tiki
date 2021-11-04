from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["137.184.218.185"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tiki',
        'USER': 'django',
        'PASSWORD': '8fb29345617abbec67122313e127fc21',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}