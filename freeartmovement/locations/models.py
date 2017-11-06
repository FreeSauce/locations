# Django Imports
from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Country(models.Model):
	country_name = models.CharField(max_length=20)
	country_coordinates = models.PointField(srid=4326)

	# Sets up the model manager for spatial data 
	objects = models.GeoManager()

	def __str__(self):
		return self.country_name
	class Meta():
		verbose_name_plural = 'Counrties'


class State(models.Model):
	state_name = models.CharField(max_length=20)
	country = models.ForeignKey(Country, related_name='state', null=True)

	# Sets up the model manager for spatial data 
	objects = models.GeoManager()


	def __str__(self):
		return self.state_name
	class Meta():
		verbose_name_plural = 'States'

class City(models.Model):
	city_name = models.CharField(max_length=20)
	city_coordinates = models.PointField(srid=4326)
	state = models.ForeignKey(State, related_name='city', null=True, blank=True)
	country = models.ForeignKey(Country, related_name='city', null=True)

	# Sets up the model manager for spatial data 
	objects = models.GeoManager()


	def __str__(self):
		return self.city_name
	
	class Meta():
		verbose_name_plural = 'Cities'
		ordering = ['-country']
