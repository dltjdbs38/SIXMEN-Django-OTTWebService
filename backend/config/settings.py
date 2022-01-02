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

env = os.environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! 
SECRET_KEY = env.get("DJANGO_SECRET_KEY", default="secret key here") 
# print(SECRET_KEY) 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] # ALLOWED_HOSTS 는 원하는 호스트가 접근할 수 있도록 설정
# ( * 은 모든 호스트가 접근 가능합니다)

APPEND_SLASH=False
# react는 SPA라 /가 필요 없다. 원래 True로 자동설정이라
# 이렇게 주소 접근하면 페이지를 찾을 수 없어서 False로 준다.

# Application definition

# 1. 웹 브라우저의 http://localhost/ (127.0.0.1:8000)를 실행하면 내 앱(user)의 함수들을 호출할 수 있게 위해 settings.py와 urls.py에 앱을 추가해주어야 합니다.

INSTALLED_APPS = [
    'user',
    'small_theater', # 추가
    'contents_analysis', # 추가
    'rest_framework', # 추가
    'drf_yasg', # 추가
    'corsheaders', # CORS 리엑트3000번 장고8000번
    # Port 번호 다르면 다른 서버로 인식하기때문에 Cross Domain 에러가 발생한다.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # 추가
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS
# 1. 배포용일 경우 'google.com' , 'hostname.example.com' 등
CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:3000', 'http://localhost:3000']
# 2. 개발일 경우
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

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

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'ott_service_database',  # DB이름                
        'USER': 'seoyoon1', # DB로그인 유저명                          
        'PASSWORD': 'seoyoon1234',  #DB로그인 비밀번호    
        'HOST': '172.27.202.145',  # 얘는 내 윈도우데스크탑 켜고끌때마다 바뀜                   
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

# AUTH_USER_MODEL = 'user.User' # 속성은 User가 가지고 있는게 아니라 User가 상속받는 AbstractUser가 다 가지고 있다. 즉, User는 기능이 없는 깡통 수준이고, 장고 내부에 세팅된 값이라 변경도 불가능하다.

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False
# 이걸 False로 해야 우리나라 시간을 가져온다

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
