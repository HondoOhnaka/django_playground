from django.forms import ModelForm
from django_playground.models import Playground

class PlaygroundForm(ModelForm):
	class Meta:
		model = Playground