# Django Imports
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin

# App Imports
from accounts.models import User
from drops.models import ArtPiece
from accounts.forms import SignupForm




# Create your views here.

def signup(request):
	""" User signup view that uses the SignupForm with the location field. """
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request,user)
			return redirect('dashboard')
	else:
		form = SignupForm()
	return render(request, 'open-pages/signup.html', {'form':form})

def dashboard(request):
	""" The dashboard view is the first view seen after log in. """
	drops = ArtPiece.objects.filter(city=request.user.location)
	users_in_town = User.objects.filter(location=request.user.location).exclude(username=request.user)
	return render(request, 'secured-pages/dashboard.html', {'users':users_in_town, 'drops':drops})

class DashboardPageView(LoginRequiredMixin, TemplateView):
	""" Uses TempalteView to render dashboard page. """
	template_name ='secured-pages/dashboard.html'	