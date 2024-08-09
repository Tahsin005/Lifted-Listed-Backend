from pathlib import Path
import os
import dj_database_url
import environ
env = environ.Env()
environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gu*2a3by4s2n)=m%tjt9+^)#rmjen6^)o)8xm3$9dkxf#&)b=c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    'https://shortlisted-iol7.onrender.com',
    'https://*.127.0.0.1',
    'http://127.0.0.1:5500',
]
CORS_ALLOW_HEADERS = [
    "content-type",
    "x-requested-with",
    "authorization",
    "x-csrftoken",
    "accept",
    "accept-encoding",
    "dnt",
    "origin",
    "user-agent",
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'corsheaders',
    
    'account',
    'product',
    'transaction',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shortlisted.urls'

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

WSGI_APPLICATION = 'shortlisted.wsgi.application'


# Database


# DATABASES = {
#     'default': {
#         #'ENGINE': 'django.db.backends.sqlite3',
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env("DB_NAME"),
#         'USER': env("DB_USER"),
#         'PASSWORD': env("DB_PASSWORD"),
#         'HOST': env("DB_HOST"),
#         'PORT': env("DB_PORT"),
#     }
# }
DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://liftedlisted_zp9r_user:Z2Vr7ec63YySKv0EQQ1dhNN1iYDJv9mV@dpg-cqr7mutsvqrc73fqush0-a.oregon-postgres.render.com/liftedlisted_zp9r',
    )
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env("DB_NAME"),
#         'USER': env("DB_USER"),
#         'PASSWORD': env("DB_PASSWORD"),
#         'HOST': env("DB_HOST"),
#         'PORT': env("DB_PORT"),
#     }
# }


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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")