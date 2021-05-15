from .base import *

DEBUG = True

ADMINS = (("Furkalo S", "furkalokbu@gmail.com"),)

ALLOWED_HOSTS = ['104.236.5.177', 'localhost']

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "portfolio_prod",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
