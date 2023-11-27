from core.config.celery import *
from core.config.cloudinary import *
from core.config.database import *
from core.config.email import *
from core.config.videosdk import *

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
