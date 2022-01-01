"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import datetime

env = os.environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! 
SECRET_KEY = env.get("DJANGO_SECRET_KEY", default="secret key here") 
#print(SECRET_KEY)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

APPEND_SLASH=False
#react의 경우 SPA라 /가 필요 없는데, 원래 True로 자동 설정이라
#이렇게 주소 접근하면 페이지를 찾을 수 없기 때문에.

CORS_ORIGIN_WHITELIST=['http://localhost:3000']
#corsheaders로 django와 react(3000번포트) 연결.


# Application definition

REST_FRAMEWORK={
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
        #첫번째는 인증된 회원만, 두번째는 모든 사람 접근 허용.
    ],
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    #api가 실행 됐을때 인증할 클래스를 정의.
    #jwt로 인증을 할거니까 api가 실행되면 jwt로 인증을 실행.
    ),
}

JWT_AUTH={
    'JWT_SECRET_KEY':SECRET_KEY,#비밀키 설정
    'JWT_ALGORITHM':'HS256',#암호화 알고리즘
    'JWT_VERIFY_EXPIRATION':True,#토큰 검증
    'JWT_ALLOW_REFRESH':True,#유효기간에 딸느 새로운 토큰 반환
    'JWT_EXPIRATION_DELTA':datetime.timedelta(minutes=30),#access토큰 만료시간
    'JWT_REFRESH_EXPIRATION_DELTA':datetime.timedelta(days=3),#refresh토큰 만료시간.
    'JWT_RESPONSE_PAYLOAD_HANDLER':'api.custom_responses.my_jwt_response_handler'
    #?
}



INSTALLED_APPS = [
    'user',
    'rest_framework',
    'rest_framework_jwt',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',    
        'NAME': 'ott_service_database',                  
        'USER': 'root',                          
        'PASSWORD': '2140',                  
        'HOST': '172.25.99.8',                     
        'PORT': '3306',                          
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

LANGUAGE_CODE = 'ko-kr'
#영어에서 바꿈

TIME_ZONE = 'Asia/Seoul'
#시간 기준을 서울로 맞춤.

USE_I18N = True

USE_L10N = True

USE_TZ = False
#이걸 False로 해야 우리나라 시간을 가져온다고 함.


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
