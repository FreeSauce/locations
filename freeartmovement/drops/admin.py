from django.contrib import admin
from . import models

# Register your models here.
class ArtPieceAdmin( admin.ModelAdmin):
	""" The editing of the ArtPiece model in the Admin. """
	fields = ('creator','title','city','likes','url_slug')
	readonly_fields = ['likes']
	prepopulated_fields = {"url_slug": ("title",)}


admin.site.register(models.ArtPiece, ArtPieceAdmin)