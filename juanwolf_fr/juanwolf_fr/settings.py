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


##############################################################################
#                              ENV VARIABLES                                 #
##############################################################################
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

SECRET_KEY = os.environ.get('SECRET_KEY', 'qwerty1234567890')

DATABASE_USER = os.environ.get('DATABASE_USER', 'postgres')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'postgres')
DATABASE_HOST = os.environ.get('DATABASE_HOST', '')
DATABASE_PORT = os.environ.get('DATABASE_PORT', '5432')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', '')

SENTRY_PROTOCOL = os.environ.get('SENTRY_PROTOCOL', '')
SENTRY_USER = os.environ.get('SENTRY_USER', '')
SENTRY_PASSWORD = os.environ.get('SENTRY_PASSWORD', '')
SENTRY_URL = os.environ.get('SENTRY_URL', '')

SENTRY_USED = SENTRY_URL != ''

current_dir = os.path.dirname(__file__)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

RAVEN_CONFIG = {
    'dsn': '%s://%s:%s@%s' % (
        SENTRY_PROTOCOL,
        SENTRY_USER,
        SENTRY_PROTOCOL,
        SENTRY_URL
    ),
}

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    'blog.juanwolf.fr', "juanwolf.fr", "resume.juanwolf.fr", "127.0.0.1",
    'localhost'
]

INTERNAL_IPS = ['127.0.0.1', '0.0.0.0']

# Application definition
INSTALLED_APPS = (
    'modeltranslation',
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
    'rest_framework_swagger',
)

if SENTRY_USED:
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)


MIDDLEWARE_CLASSES = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

# ADD DEBUG OPTIONS
if DEBUG:
    INSTALLED_APPS = ('debug_toolbar',) + INSTALLED_APPS

    MIDDLEWARE_CLASSES = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE_CLASSES

SITE_ID = 1

ROOT_URLCONF = 'juanwolf_fr.urls'

WSGI_APPLICATION = 'juanwolf_fr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
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
STATIC_ROOT = '/srv/http/static/'

STATIC_URL = '/static/'

DEBUG_TOOLBAR_PATCH_SETTINGS = True


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "media"),
    os.path.join(BASE_DIR, 'static')
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
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'blogengine.template_context_preprocessor.get_categories'
            ]
        }
    },
]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            },
        },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

# Summernote configuration
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': True,

    # Using Summernote Air-mode
    'airMode': False,

    # Change editor size
    'width': '100%',
    'height': '650',

    # Or, set editor language/locale forcely
    'lang': 'fr-FR',
    'external_js': (
        '//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js'
    ),
    'internal_js': (
        '/static/js/main.min.js',
    )
}

# CUSTOM
BIRTHDAY_DATE = date(year=1992, month=9, day=26)
