import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokedex.settings')

app = Celery('pokedex')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

print('Celery Config Loaded:')
print(app.conf)

@app.task(bind=True)
def load_pokedex(name, url):
    print(f'Loading pokemon {name} using {url}')
