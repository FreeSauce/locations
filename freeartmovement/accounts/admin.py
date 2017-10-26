# Python Imports
from django.contrib import admin
# Relative Imports
from .models import User

# Registering models for the admin
admin.site.register(User)