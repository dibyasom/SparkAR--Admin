import os

from sparkar.settings.base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ["*"]

DEBUG = True

# SOCIAL_AUTH_GITHUB_KEY = "6f89338e548987acd8da"
# SOCIAL_AUTH_GITHUB_SECRET = "cc54b17010c071fb6f92dd85651a5bfaf62f8043"
SOCIAL_AUTH_GITHUB_KEY = "7e73e8da74b45fda52ce"
SOCIAL_AUTH_GITHUB_SECRET = "c5e9783855b293003f144653392976b4213330cb"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "default",
    }
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": "5432",
    }
}

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "home/static"),
]

MEDIA_URL = "media/"
MEDIA_ROOT = "media"
