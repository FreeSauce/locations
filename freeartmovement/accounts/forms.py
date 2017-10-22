from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm

from locations.models import City


class SignupForm(UserCreationForm):
	location = forms.ModelChoiceField(queryset=City.objects.all(), required=True, initial=1)

	class Meta:
		model = User
		fields = ['username','location','password1','password2']

	def save (self, commit=True):
		user = super(SignupForm, self).save(commit=False)

		if commit:
			user.save()

		return user