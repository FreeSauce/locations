# Django Imports
from django.contrib import admin

# App Imports
from leaflet.admin import LeafletGeoAdmin

# Relative Imports
from .models import HintStation



# Register your models here.
class StationAdmin( LeafletGeoAdmin):
	list_display = ('station_name','city','activation_status')

admin.site.register(HintStation, StationAdmin)