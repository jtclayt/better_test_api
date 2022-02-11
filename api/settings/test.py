from .base import *

SECRET_KEY = 'django-insecure-%_=*gz*-c$v2kg!a(2s$!26dbi#qdg-dra@szh=rvu+j&0ulop'

DEBUG = False

ALLOWED_HOSTS = ['localhost']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db'
    }
}
