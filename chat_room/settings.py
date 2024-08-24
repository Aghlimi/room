from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-vz%+)1t3q06_eo4^h+je+bj^$ke1vwm_v@klf8o-w=)@+h-2#^"
DEBUG = True
ALLOWED_HOSTS = ["192.168.168.1", "127.0.0.1", "192.168.98.53","192.168.38.1"]
INSTALLED_APPS = [
    "app",
    "Accounts",
    "post",
    "chat",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "chat_room.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates", "Accounts/templates", "app/templates", "post/templates"],
        "APP_DIRS": 1,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "chat_room.wsgi.application"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "mydata",
#         "USER": "aghlimi",
#         "PASSWORD": "1234",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "post/static"),
    os.path.join(BASE_DIR, "chat_room/static"),
    os.path.join(BASE_DIR, "Accounts/static"),
]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "media/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
