from accounts.forms import SignupForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from accounts.models import User


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
	return render(request, 'signup.html', {'form':form})

def dashboard(request):
	users_in_town = User.objects.filter(location=request.user.location).exclude(username=request.user)
	return render(request, 'dashboard.html', {'users':users_in_town})