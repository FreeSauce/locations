# Django Imports
from django import forms
# Relative Imports
from .models import ArtPiece, Hint

class ArtPieceForm(forms.ModelForm):
	class Meta:
		model = ArtPiece
		fields = ['title','preview_image']


class Form1(forms.ModelForm):
	class Meta:
		model= Hint
		fields = ['artpiece','riddle']

class Form2(forms.ModelForm):
	class Meta:
		model= Hint
		fields = ['gps_coords']