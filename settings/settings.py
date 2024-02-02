"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from yaml import safe_load


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

f = open(BASE_DIR / 'config.yaml', 'r')
config = safe_load(f)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i=w!tyt-_zv1(0aj3%n_1@qwri1jhaw5c%4tjqs=jcy%0tx0g#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0"
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
# Application definition

INSTALLED_APPS = [
    # builtins
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # site-packages
    "debug_toolbar",

    # My packages
    'repricer',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware"
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': "marketprod",
#         'USER': "user",
#         'PASSWORD': "example",
#         'HOST': "pg",
#         'PORT': 5432,
#     }
# }
DATABASES = {
    'default': {
        # String. It must be "mssql".
        'ENGINE': 'mssql',

        # String. Database name. Required.
        'NAME': 'marketprod',

        # String. Database user name in "user" format. If not given then MS Integrated Security will be used.
        'USER': config['marketserver_sql']['login']
,

        # String. Database user password.
        'PASSWORD': config['marketserver_sql']['pass'],

         # String. SQL Server instance in "server\instance" format.
        'HOST': '192.168.22.224',

        # String. Server instance port. An empty string means the default port.
        'PORT': '',

        # Dictionary. Additional database settings.
        'OPTIONS': {
            # String. ODBC Driver to use ("ODBC Driver 17 for SQL Server",
            # "SQL Server Native Client 11.0", "FreeTDS" etc).
            # Default is "ODBC Driver 17 for SQL Server".
            # 'Trusted_Connection': 'no',
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_RESULT_BACKEND = "rpc://"
CELERY_RESULT_PERSISTENT = True

# login
AUTH_USER_MODEL = 'users.MpUser'

LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'