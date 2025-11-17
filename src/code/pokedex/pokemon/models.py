import json
import requests

from django.db import models


## Helper functions
def get_hp_from_stats(stats_dict):
    hp_gen = filter(lambda x: x['stat']['name'] == 'hp', stats_dict)
    hp_stat = list(hp_gen)[0]

    return hp_stat['base_stat']


class Pokemon(models.Model):
    name = models.CharField()
    main_type = models.CharField()
    base_hp = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    create_timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def create_from_api_url(url):
        resp = requests.get(url)
        poke_dict = json.loads(resp.content)

        return Pokemon(
            main_type=poke_dict['types'][0]['type']['name'],
            base_hp=get_hp_from_stats(poke_dict['stats']),
            height=poke_dict['height'],
            weight=poke_dict['weight']
        )
