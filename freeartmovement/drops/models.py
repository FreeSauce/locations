from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

from locations.models import City

# Create your models here.
class ArtPiece(models.Model):

	READY = 'Ready to Drop'
	DROPPED = 'Dropped!'
	# A list of choices	
	DROP_STATUS_CHOICES = ((READY, 'Ready to Drop'), (DROPPED, 'Dropped!'),)


	creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
	title = models.CharField(max_length=80, unique=True)
	city = models.ForeignKey(City, related_name='artpiece')
	created_at = models.DateTimeField(auto_now_add=True)
	uuid = models.CharField(max_length=36, null=True)
	trimmed_uuid = models.CharField(max_length=8, null=True)
	status = models.CharField(max_length=11, choices=DROP_STATUS_CHOICES, default=READY)

	url_slug = models.SlugField(blank=True)
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