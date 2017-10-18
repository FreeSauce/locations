from django.contrib import admin
from .models import Country, State, City

# Register your models here.
class CityAdmin( admin.ModelAdmin):
	list_display = ('city_name','state','country')

admin.site.register(Country)
admin.site.register(City, CityAdmin)
admin.site.register(State)

