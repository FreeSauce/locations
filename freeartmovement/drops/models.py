# Python Imports
import uuid
# Django Imports
from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
from django.template.defaultfilters import slugify
# App Imports
from locations.models import City

# Create your models here.

def create_uuid():
	return str(uuid.uuid4())

def user_uploads(instance, filename):
	""" Constructs a file system path for user uploads. """
	return '%Y/%b/{0}/{1}'.format(instance.creator,filename)

class ArtPiece(models.Model):
	READY = 'Ready to Drop'
	DROPPED = 'Dropped!'
	# A list of choices	
	DROP_STATUS_CHOICES = ((READY, 'Ready to Drop'), (DROPPED, 'Dropped!'),)

	creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
	title = models.CharField(max_length=80, unique=True, blank=False, null=False)
	preview_image = models.ImageField(upload_to=user_uploads, default='stock/stealth_drop.png')
	city = models.ForeignKey(City, related_name='artpiece', null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	uuid = models.CharField(max_length=36, default=create_uuid)
	status = models.CharField(max_length=13, choices=DROP_STATUS_CHOICES, default=READY)

	url_slug = models.SlugField(blank=False)
	likes = models.IntegerField(default=0)


	def __str__(self):
		""" A string representation of the ArtPiece model for readability. """
		return self.title

	def save(self, *args, **kwargs):
		""" The ArtPiece save method is overwritten to incorporate a slug. """
		self.url_slug = slugify(self.title)
		super(ArtPiece, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-created_at']

class Hint(models.Model):
	""" Every art piece needs to be associated with hints."""
	artpiece = models.OneToOneField(ArtPiece, on_delete=models.CASCADE)
	riddle = models.TextField()
	gps_coords = models.PointField(srid=4326, null=True)	

	
	def __str__(self):
		return "Hints for {}".format(self.artpiece.title)

	def hints_to_dict(self):
		return {'riddle':self.riddle,'map_clue':self.gps_coords}