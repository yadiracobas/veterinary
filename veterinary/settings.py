# coding=utf-8
from __future__ import absolute_import

import os
import sys
from unipath import Path

BASE_DIR = Path(__file__).ancestor(2)

sys.path.append(BASE_DIR.child("apps"))

SECRET_KEY = 'jd4j41)fnv+ydkz^etcgn9qw(hnyqwux-gn7(%ylqj0adok%_n'

DEBUG = True

ALLOWED_HOSTS = ['*']

DJANGO_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'generals',
    'geo',
    'userprofiles'
]

THIRD_PARTY_APPS = []

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'veterinary.urls'

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

WSGI_APPLICATION = 'veterinary.wsgi.application'

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

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'userprofiles.User'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_ROOT = os.path.join(BASE_DIR, "static")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'veterinary',
        'USER': 'root',
        'PASSWORD': 'adminadmin',
        'HOST': 'localhost',
        'PORT': '',
    }
}

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'cobas.carbonell@gmail.com'

EMAIL_HOST_PASSWORD = 'C@rb0n311'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

JET_DEFAULT_THEME = 'light-blue'

JET_SIDE_MENU_CUSTOM_APPS = [
    ('auth',[
        'Group',
    ]),
    ('userprofiles',[
        'User',
    ])
]