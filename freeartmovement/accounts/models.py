# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractUser
# App Imports
from locations.models import City


class User(AbstractUser):
	""" Overwrote the User model to include a location field. """
	location = models.ForeignKey(City, related_name="user_location", null=True)
	
