from accounts.forms import SignupForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from accounts.models import User
from drops.models import ArtPiece


# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request,user)
			return redirect('dashboard')
	else:
		form = SignupForm()
	return render(request, 'open/signup.html', {'form':form})

def dashboard(request):
	drops = ArtPiece.objects.filter(city=request.user.location)
	users_in_town = User.objects.filter(location=request.user.location).exclude(username=request.user)
	return render(request, 'secured/dashboard.html', {'users':users_in_town, 'drops':drops})