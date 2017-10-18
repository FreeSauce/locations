from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from locations.models import City

# Create your models here.
class ArtPiece(models.Model):
	creator = models.ForeignKey(User, null=False)
	title = models.CharField(max_length=80)
	city = models.ForeignKey(City, related_name='artpiece')
	created_at = models.DateTimeField(auto_now_add=True)
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