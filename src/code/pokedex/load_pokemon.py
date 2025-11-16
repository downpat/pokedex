from celery import Celery

from pokemon.models import Pokemon

redis_pass = "gottaC47TCHem477"

app = Celery('load_pokemon', broker=f'redis://:{redis_pass}@192.168.165.26:6379/0')

@app.task
def load_pokemon(name, url):
    print(f'Loading pokemon {name} using {url}')
