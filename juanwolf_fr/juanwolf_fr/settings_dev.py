"""
Django settings for juanwolf_s_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from datetime import date
from configparser import RawConfigParser

import django.conf.global_settings as DEFAULT_SETTINGS

config = RawConfigParser()
current_dir = os.path.dirname(__file__)
config.read('%s/settings.ini' % current_dir)


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('secrets', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'blog.zell']

INTERNAL_IPS = ['127.0.0.1']

# Application definition
INSTALLED_APPS = (
    'modeltranslation',
    'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.syndication',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django_summernote',
    'django_jenkins',
    'blogengine',
    'resume',
    'rest_framework',
    'rest_framework_swagger'
)


MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

SITE_ID = 1

ROOT_URLCONF = 'juanwolf_fr.urls'

WSGI_APPLICATION = 'juanwolf_fr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config.get('database', 'DATABASE_NAME'),
        'USER': config.get('database', 'DATABASE_USER'),
        'PASSWORD': '',
        'HOST': '',  # Empty for localhost through domain sockets or 127.0.0.1
        'PORT': '5432',  # Set to empty string for default.
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

USE_TZ = True
TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True
LANGUAGES = (
    ('en', 'English'),
    ('fr', 'Français'),
)

LOCALE_PATHS = ('conf/locale/',)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# STATIC_ROOT = '/home/juanwolf/juanwolf.fr/'

STATIC_URL = '/static/'

DEBUG_TOOLBAR_PATCH_SETTINGS = True


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "media"),
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

# Template directory
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, 'juanwolf_fr', 'templates')
        ],
        'OPTIONS': {
            'context_processors': (
                DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + [
                    'blogengine.template_context_preprocessor.get_categories'
                ]
            )
        }
    },
]


# Summernote configuration
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': False,

    # Using Summernote Air-mode
    'airMode': False,

    # Change editor size
    'width': '100%',
    'height': '650',

    # Or, set editor language/locale forcely
    'lang': 'fr-FR',
    'external_js': (
        '//juanwolf.fr/js/lib/JQuery1.11.js',
        '//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js'
    )
}

# CUSTOM
BIRTHDAY_DATE = date(1992, 9, 26)
