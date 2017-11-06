# Django Imports
from django.contrib import admin
# App Imports
from leaflet.admin import  LeafletGeoAdmin, LeafletGeoAdminMixin 
# Relative Imports
from . import models

# Register your models here.
class HintAdmin(LeafletGeoAdmin):
	pass

class HintInline(LeafletGeoAdminMixin, admin.StackedInline):
	""" The HintInline is added to the ArtPiece AdminModel for easy editting. """
	model = models.Hint
	extra = 1
	fields = ('riddle','gps_coords')


class ArtPieceAdmin( admin.ModelAdmin):
	""" The editing of the ArtPiece model in the Admin. """
	fields = ('creator','preview_image','title','city','status','likes','uuid','url_slug')
	readonly_fields = ['likes','uuid',]
	prepopulated_fields = {"url_slug": ("title",)}
	inlines = [HintInline,]

# Registration of models in the Admin.
admin.site.register(models.ArtPiece, ArtPieceAdmin)
admin.site.register(models.Hint, HintAdmin)
