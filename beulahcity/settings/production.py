from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['BEULAH_SECRET_KEY']

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['.beulahcity.com',
                 '.beulahcity.co.ke']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AWS_STORAGE_BUCKET_NAME = os.environ['BEULAH_AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


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
