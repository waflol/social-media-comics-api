import os

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DB_ENGINE = os.environ.get("DB_ENGINE", None)
DB_NAME = os.environ.get("DB_NAME", None)
DB_USER = os.environ.get("DB_USER", None)
DB_PASSWORD = os.environ.get("DB_PASSWORD", None)
DB_HOST = os.environ.get("DB_HOST", None)
DB_PORT = os.environ.get("DB_PORT", None)

if DB_ENGINE is None or DB_ENGINE == "sqlite3":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends." + DB_ENGINE,
            "NAME": DB_NAME,
            "USER": DB_USER,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
        },
    }
