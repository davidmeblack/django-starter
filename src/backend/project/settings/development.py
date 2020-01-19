from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DEBUG = True

SECRET_KEY = config('DJANGO_SECRET_KEY_DEV')
