# Python Imports
# Django Imports
# App Imports
# Relative Imports

from django.db import models

# Create your models here.

class Country(models.Model):
	country_name = models.CharField(max_length=20)
	country_longitude = models.DecimalField(max_digits=11, decimal_places=8)
	country_latitude = models.DecimalField(max_digits=11, decimal_places=8)

	def __str__(self):
		return self.country_name
	class Meta():
		verbose_name_plural = 'Counrties'

class State(models.Model):
	state_name = models.CharField(max_length=20)
	state_longitude = models.DecimalField(max_digits=11, decimal_places=8)
	state_latitude = models.DecimalField(max_digits=11, decimal_places=8)
	country = models.ForeignKey(Country, related_name='state', null=True)

	def __str__(self):
		return self.state_name
	class Meta():
		verbose_name_plural = 'States'

class City(models.Model):
	city_name = models.CharField(max_length=20)
	city_longitude = models.DecimalField(max_digits=11, decimal_places=8)
	city_latitude = models.DecimalField(max_digits=11, decimal_places=8)	
	state = models.ForeignKey(State, related_name='city', null=True, blank=True)
	country = models.ForeignKey(Country, related_name='city', null=True)
	def __str__(self):
		return self.city_name
	
	class Meta():
		verbose_name_plural = 'Cities'
		ordering = ['-country']
