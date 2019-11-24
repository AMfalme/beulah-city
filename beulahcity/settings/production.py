from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['BEULAH_SECRET_KEY']

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['.beulahcity.com', '.beulahcity.co.ke', '.mizizi.io']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['BEULAH_WAGTAIL_DB'],
        'USER': os.environ['WAGTAIL_DB_USER'],
        'PASSWORD': os.environ['WAGTAIL_DB_PASS'],
        'HOST': os.environ['WAGTAIL_DB_HOST'],
        'PORT': os.environ['WAGTAIL_DB_PORT'],
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': './debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

try:
    from .local import *
except ImportError:
    pass
