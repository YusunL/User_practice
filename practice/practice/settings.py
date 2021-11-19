"""
Django settings for practice project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from .my_settings import SECRET_KEY
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'app.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_jwt',
    'app',
]

REST_FRAMEWORK = {
    # 인증된 유저만 헤더에 access token 을 포함하여 유효한 유저만이 접근이 가능해지는 것을 디폴트로. permission_classes 변수 설정할 필요가 없음.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # 인증된 회원만 엑세스 허용
        'rest_framework.permissions.AllowAny',         # 모든 회원 액세스 허용
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication', # api 실행시 인증할 클래스 정의
    ),
}


SIMPLE_JWT = {

    # 여기는 기본 세팅값

    'JWT_SECRET_KEY': SECRET_KEY,  # JWT 에 서명하는데 사용되는 시크릿키. 장고의 시크릿키가 디폴트.
    'JWT_ALGORITHM': 'HS256',  # PyJWT 에서 암호화 서명에 지원되는 알고리즘으로 마찬가지로 이것 또한 기본값.
    'JWT_VERIFY_EXPIRATION': True,  # 토큰 만료 시간 확인. 기본값 True.

    # 새로 커스텀한 옵션들

    'JWT_ALLOW_REFRESH': True,  # 토큰 새로고침 기능 활성화. 기본값 False.
    'JWT_EXPIRATION_DELTA': timedelta(minutes=30),  # datetime.timedelta 의 만료 시간. 기본값 seconds=300.
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=3),  # Refresh Token의 새로 고침 시간. 기본값 days=7
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'accounts.custom_responses.my_jwt_response_handler'
    # 로그인 또는 새로 고침 후 반환되는 응답 데이터를 제어. 기본값은 {'token' : token } 인데 이건 나중에 우리가 따로 적어줄것임.
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'practice.urls'

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

WSGI_APPLICATION = 'practice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
