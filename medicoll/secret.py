"""
Here will be stored some secret information, like
secret keys, allowed host, debug mode etc.
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'm*5**2d61dh8%d!0fescj+hqwy0gg@vtqu+bf-x9o4hd_=q@37'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
