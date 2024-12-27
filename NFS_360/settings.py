"""
Django settings for NFS_360 project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qy6%-%f%kd6p+9g7c=u)j3v+zs3h0h*u(mhx+(vss=tnx)!s)c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App_User',
    'App_User.templatetags',
    'App_Admin',
    'App_Superuser',
    # 'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    # 'channels',  # Required for Django-Plotly-Dash
    # 'rest_framework',  # Optional but recommended
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_plotly_dash.middleware.BaseMiddleware',
    # 'django_plotly_dash.middleware.ExternalRedirectionMiddleware',
    # 'NFS_360.middleware.UniqueURLMiddleware',  # Add this line
]


# # Channels settings for WebSocket support (Django-Plotly-Dash)
# ASGI_APPLICATION = 'NFS_360.asgi.application'
 
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"
#     }
# }

ROOT_URLCONF = 'NFS_360.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'NFS_360.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mssql',  # Adjust as needed for your backend
        'NAME': os.environ.get('DATABASE_NAME', 'neucode-sql-dev'),
        'USER': os.environ.get('DATABASE_USER', 'neucodeadmin'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'AASU@123'),
        'HOST': os.environ.get('DATABASE_HOST', 'neucode-server-dev.database.windows.net'),
        'PORT': os.environ.get('DATABASE_PORT', '1433'),  # Default MSSQL port
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
            'Encrypt': 'yes',
            'TrustServerCertificate': 'yes',
        },
    }
}

# Email Configuration using environment variables
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.office365.com')  # Replace with a default if needed
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))  # Default to port 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'anantsol@neucodetalent.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'AgtQb@24')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'App_Admin/static'),  # Ensure this matches your project structure
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


