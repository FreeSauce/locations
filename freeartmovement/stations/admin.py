from django.contrib import admin
from .models import HintStation

# Register your models here.
class StationAdmin( admin.ModelAdmin):
	list_display = ('station_name','city','activation_status')

admin.site.register(HintStation, StationAdmin)