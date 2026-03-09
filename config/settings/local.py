from .base import *  # noqa: F403,F401

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"