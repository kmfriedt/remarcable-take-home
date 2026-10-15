import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")


# AI was asked what I needed to include for security and default database
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}