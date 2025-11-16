from django.db import models

class Pokemon(models.Model):
	name = models.CharField()
	main_type = models.CharField()
	base_hp = models.IntegerField()
	height = models.IntegerField()
	weight = models.IntegerField()
	create_timestamp = models.DateTimeField(auto_now_add=True)
