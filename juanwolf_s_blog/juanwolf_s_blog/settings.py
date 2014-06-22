"""
Django settings for juanwolf_s_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django.conf.global_settings as DEFAULT_SETTINGS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&n7c--zvj(gzrufi08464k1y1$teq052d=o#u7_+^9s+3+)5ot'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['blog.juanwolf.fr', 'localhost', '127.0.0.1',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'blogengine',
    'django.contrib.syndication',
    'django_summernote',
    'modeltranslation',
    'django.contrib.sites',
    'django.contrib.sitemaps',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

SITE_ID = 1

ROOT_URLCONF = 'juanwolf_s_blog.urls'

WSGI_APPLICATION = 'juanwolf_s_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'juanwolfsBlogDB',
        'USER': 'bibaskend',
        'PASSWORD': '',
        'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432', # Set to empty string for default.
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
STATIC_ROOT = '/home/juanwolf/juanwolf.fr/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home/juanwolf/juanwolf.fr/',
)

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

# Template directory
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'blogengine.template_context_preprocessor.get_current_path',
)

# Summernote configuration
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': True,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Using Summernote Air-mode
    'airMode': False,

    # Change editor size
    'width': '100%',
    'height': '450',

    # Or, set editor language/locale forcely
    'lang': 'fr-FR',
}
