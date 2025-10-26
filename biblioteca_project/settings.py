"""
Django settings for biblioteca_project project.
Generado para el proyecto de Sistema de Gestión de Biblioteca Virtual
"""

from pathlib import Path

# BASE_DIR apunta al directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta (solo para desarrollo)
SECRET_KEY = 'django-insecure-biblioteca-virtual-1234567890'

# Modo de depuración
DEBUG = True

ALLOWED_HOSTS = []


# ------------------------------------------------------------
# APLICACIONES INSTALADAS
# ------------------------------------------------------------
INSTALLED_APPS = [
    # Apps principales de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',

    # App local
    'core',  # 👈 Tu aplicación donde estarán los modelos de libros, usuarios, etc.
]


# ------------------------------------------------------------
# MIDDLEWARE
# ------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ------------------------------------------------------------
# CONFIGURACIÓN PRINCIPAL DEL PROYECTO
# ------------------------------------------------------------
ROOT_URLCONF = 'biblioteca_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Carpeta donde se guardarán las plantillas HTML
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'biblioteca_project.wsgi.application'


# ------------------------------------------------------------
# BASE DE DATOS (usaremos SQLite por simplicidad)
# ------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ------------------------------------------------------------
# VALIDADORES DE CONTRASEÑA
# ------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ------------------------------------------------------------
# CONFIGURACIÓN DE IDIOMA Y ZONA HORARIA
# ------------------------------------------------------------
LANGUAGE_CODE = 'es-mx'  # español (México)

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True
USE_TZ = True


# ------------------------------------------------------------
# ARCHIVOS ESTÁTICOS (CSS, JS, IMÁGENES)
# ------------------------------------------------------------
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Carpeta donde se guardarán archivos subidos por el usuario (como imágenes de libros)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ------------------------------------------------------------
# CONFIGURACIÓN FINAL
# ------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',  # Solo JSON
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

