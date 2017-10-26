# Python Imports
# Django Imports
# App Imports
# Relative Imports

from django.shortcuts import render

# Create your views here.
def home(request):
	""" The home view returns the no auth required home.html template"""
	return render(request, 'open-pages/home.html')

def about(request):
	""" The about view returns the no auth required about.html template"""
	return render(request, 'open-pages/about.html')

def contact(request):
	""" The contact view returns the no auth required contact_us.html template"""
	return render(request, 'open-pages/contact_us.html')

def login(request):
	""" The login view returns the login.html template"""
	return render(request, 'open-pages/login.html')

def signup(request):
	""" The signup view returns the signup.html template"""
	return render(request, 'open-pages/signup.html')