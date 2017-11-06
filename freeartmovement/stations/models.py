# Django Imports
from django.db import models
from django.contrib.gis.db import models

# App Imports
from locations.models import City

# Create your models here.
class HintStation(models.Model):
	station_name = models.CharField(max_length = 10, primary_key=True)
	city = models.ForeignKey(City, related_name='station')
	station_coordinates = models.PointField(srid=4326)
	activation_status = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	visitor_count = models.IntegerField(default=0)

	# Sets up the model manager for spatial data 
	objects = models.GeoManager()

	def __str__(self):
		""" A string representation of the HintStation model for readability. """
		return self.station_name

	class Meta():
		verbose_name_plural = 'Hint Stations'