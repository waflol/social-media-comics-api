import os

from core.config.celery import *
from core.config.cloudinary import *
from core.config.database import *
from core.config.email import *
from core.config.sentry import *
from core.config.videosdk import *

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(" ")
CORS_ORIGIN_WHITELIST = os.environ.get("CORS_ORIGIN_WHITELIST").split(" ")
