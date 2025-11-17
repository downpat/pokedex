from celery import shared_task

from .models import Pokemon

@shared_task
def load_pokemon(name, url):
    p = Pokemon.create_from_api_url(url)
    p.name = name
    p.save()

