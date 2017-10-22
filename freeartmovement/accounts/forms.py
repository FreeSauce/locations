from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm

from locations.models import City


class SignupForm(UserCreationForm):
	location = forms.ModelChoiceField(queryset=City.objects.all(), required=True, initial=1)
	email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())


	class Meta:
		model = User
		fields = ['username','email','location','password1','password2']

	def save (self, commit=True):
		user = super(SignupForm, self).save(commit=False)

		if commit:
			user.save()

		return user