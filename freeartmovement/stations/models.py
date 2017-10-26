# Python Imports
# Django Imports
# App Imports
# Relative Imports
from django.db import models
from locations.models import City

# Create your models here.
class HintStation(models.Model):
	station_name = models.CharField(max_length = 10, primary_key=True)
	city = models.ForeignKey(City, related_name='station')
	station_longitude = models.DecimalField(max_digits=11, decimal_places=8)
	station_latitude = models.DecimalField(max_digits=11, decimal_places=8)
	activation_status = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	visitor_count = models.IntegerField(default=0)

	def __str__(self):
		""" A string representation of the HintStation model for readability. """
		return self.station_name

	class Meta():
		verbose_name_plural = 'Hint Stations'