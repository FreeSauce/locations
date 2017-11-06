# Python Imports
# Django Imports
from django.contrib import admin

# App Imports
from leaflet.admin import LeafletGeoAdmin

# Relative Imports
from .models import Country, State, City

# Register your models here.
class CityAdmin(LeafletGeoAdmin):
	list_display = ('city_name','state','country')

class CountryAdmin(LeafletGeoAdmin):
	list_display = ('country_name','country_coordinates')

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(State)

