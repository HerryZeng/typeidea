from .base import *  # NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOBAR_PANELS = [
    'djdt_flamegraph.FlamegraphPanel',
]
