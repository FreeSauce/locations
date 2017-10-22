from django.db import models
from django.contrib.auth.models import AbstractUser
from locations.models import City

class User(AbstractUser):
	location = models.ForeignKey(City, related_name="user_location", null=True)
	
