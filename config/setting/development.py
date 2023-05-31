from config.settings import *



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET_KEY = 'django-insecure-s#5(%gc1f!bsx_&yhgzk4zxm_vn060(*bih6p#_!#3&2po#0y('


DEBUG = True


ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'blog',
    'advertisment',
    
]

STATIC_ROOT = BASE_DIR.joinpath('/static')

MEDIA_ROOT = BASE_DIR.joinpath('media')


STATICFILES_DIRS = [
    BASE_DIR/'static',
    BASE_DIR/'media',
]

