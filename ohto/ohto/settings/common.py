"""
Django settings for ohto project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
#NOTE: 태그 14개인 이유: 클러스터링으로 추려낸것임을 강조
from pathlib import Path
import os
from datetime import timedelta

#TODO: add Elastic search
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v6w_8s=)_(rbclexof0=r$4epuwdm$x#wd77v$3i!0+4(q^b0x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',
    '43.200.92.0',
    'ohto.kr',
]


# Application definition

INSTALLED_APPS = [
    #django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Third Apps
    'django_extensions',
    'debug_toolbar',
    'django_bootstrap5',
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
    'drf_spectacular',
    #Local App
    'accounts',
    'music_demo'
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'ohto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'ohto','templates')
        ],
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

WSGI_APPLICATION = 'ohto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'ohto','static')
]
STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = 'media/' #NOTE: 미디어 파일 접근시
MEDIA_ROOT = os.path.join(BASE_DIR,'media') #NOTE: 미디어 파일 저장 시

AUTH_USER_MODEL = 'accounts.User'


#NOTE: REST_FRAMEWORK의 DEFAULT_PERMISSION_CLASSES로 api view에 대한 전역 접근 권한을 설정한다.
#Rest frame work로 url접근시 기본적으로 로그인 되어있고(IsAuthenticated)
#로그인 되어있지 않다면 읽기만 가능하게 설정
REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES":[
        #NOTE: 순서 꼬이면 ImportError나더라
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
    "DEFAULT_PERMISSON_CLASSES":[
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    "DEFAULT_SCHEMA_CLASS":'drf_spectacular.openapi.AutoSchema',
}
#NOTE: djangorestframework_simplejwt 설정
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'TOKEN_USER_CLASS': 'accounts.User'
}
#NOTE: api명세 drf_spectacular setting
SPECTACULAR_SETTINGS = {
    'TITLE': 'Ohto api server',
    'DESCRIPTION': 'User, Song, Playlist API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#django_debug_toolbar setting
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
#Cors config
CORS_ALLOWED_ORIGINS=[

]
CORS_ALLOW_ALL_ORIGINS=True

#TODO: s3
#TODO: 이미지 작성(도커 이미지 작성)
#TODO: 태그 추가(계절,장르)
#TODO: 테마 mbti