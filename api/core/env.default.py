# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tgwj=)h$kaiooy@im=wg!^9!em3s$$egzhsx^wuloszonc06t_'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

APP_TITLE = 'APP_TITLE'
APP_DESCRTIPTION = 'APP_DESCRTIPTION'
PROTOCOL = 'https'
DOMAIN = 'my.domain'
ALLOWED_HOSTS = [DOMAIN, '127.0.0.1']
TIME_ZONE = 'Asia/Saigon'
EMAIL_ENABLE = True
ENV = 'LOCAL'  # 'LOCAL, PROD'
IMAGE_MAX_WIDTH = 1200
IMAGE_THUMBNAIL_WIDTH = 300
IMAGE_RATIO = 1.618
UPLOAD_MAX_SIZE = 4

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'docker',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': '__app_name___db',
        'PORT': '5432',
        'TEST': {
            'NAME': 'docker_test',
        },
    },
}
LANGUAGES = []
FIRST_USER_USERNAME = 'admin'
FIRST_USER_PASSWORD = 'admin'
TEST_ADMIN = {
    'username': 'admin',
    'email': 'admin@gmail.com',
    'password': '1234567890',
    'first_name': 'First',
    'last_name': 'Admin'
}
TEST_USER = {
    "username": "tbson0",
    "email": "tbson0@gmail.com",
    "password": "123456",
    "first_name": "Son",
    "last_name": "Tran",
    "phone": "000"
}
TEST_FINGERPRINT = 'test-fingerprint'

SLACK_WEBHOOK_URL = ''

DEFAULT_FROM_EMAIL = '"{}"<admin@gmail.com>'.format(APP_TITLE)
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # 587 - 465 for SSL
EMAIL_HOST_USER = 'admin@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True
