from django.views.generic.edit import FormView
from django_playground.forms import PlaygroundForm

class PlaygroundFormView(FormView):
	template_name = 'playground_form.html'
	form_class = PlaygroundForm
	success_url = '/'
