print('Loading local settings')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pokedex',
        'USER': 'ash',
        'PASSWORD': 'gottaC47TCH#em477',
        'HOST': 'pokedex-db',
        'PORT': 5432
    }
}


REDIS_PASS = "gottaC47TCHem477"

CELERY_BROKER_URL = f'redis://:{REDIS_PASS}@pokedex-redis:6379/0'
