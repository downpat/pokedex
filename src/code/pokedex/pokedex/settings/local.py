print('Loading local settings')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pokedex',
        'USER': 'ash',
        'PASSWORD': 'gottaC47TCH#em477',
        'HOST': '192.168.165.26',
        'PORT': 5432
    }
}


REDIS_PASS = "gottaC47TCHem477"

CELERY_BROKER_URL = f'redis://:{REDIS_PASS}@192.168.165.26:6379/0'
