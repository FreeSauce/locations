# Django Imports
from django import forms
# Relative Imports
from .models import ArtPiece

class ArtPieceForm(forms.ModelForm):
	class Meta:
		model = ArtPiece
		fields = ['title','preview_image']
