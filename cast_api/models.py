from django.db import models

# Create your models here.
class Forecast(models.Model):
	city = models.CharField(max_length=32)
	state = models.CharField(max_length=32)
	notes = models.CharField(max_length=32)
    