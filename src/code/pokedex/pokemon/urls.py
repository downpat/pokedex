from django.urls import path

from .views import index, build_pokedex, full_list, single_pokemon

urlpatterns = [
    path('', index),
    path('build', build_pokedex),
    path('pokemon', full_list),
    path('pokemon/<str:name>', single_pokemon)
]
