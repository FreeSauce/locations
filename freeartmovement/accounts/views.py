from accounts.forms import SignupForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('studio')
	else:
		form = SignupForm()
	return render(request, 'signup.html', {'form':form})