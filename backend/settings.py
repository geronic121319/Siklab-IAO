import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-only-change-me")
DEBUG = os.getenv("DJANGO_DEBUG", "true").lower() == "true"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,testserver").split(",")

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "backend.transactions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "backend.middleware.database_role.DatabaseRoleMiddleware",
]

ROOT_URLCONF = "backend.urls"
TEMPLATES = []
WSGI_APPLICATION = "backend.wsgi.application"

db_engine = os.getenv("DB_ENGINE", "django.db.backends.postgresql")
DATABASES = {
    "default": (
        {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.getenv("POSTGRES_DB", str(BASE_DIR / "db.sqlite3")),
        }
        if db_engine == "django.db.backends.sqlite3"
        else {
            "ENGINE": db_engine,
            "NAME": os.getenv("POSTGRES_DB", "siklab"),
            "USER": os.getenv("POSTGRES_USER", "siklab"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD", "siklab"),
            "HOST": os.getenv("POSTGRES_HOST", "localhost"),
            "PORT": os.getenv("POSTGRES_PORT", "5432"),
        }
    )
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
