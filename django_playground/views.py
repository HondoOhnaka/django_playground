from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import Http404, HttpResponse
from django_playground.forms import PlaygroundForm
from django_playground.models import Playground
from django.core.urlresolvers import reverse

class PlaygroundCreateView(CreateView):
	template_name = 'django_playground/playground_form.html'
	form_class = PlaygroundForm
	success_url = "/playground/"

class PlaygroundUpdateView(UpdateView):
	template_name = 'django_playground/playground_form.html'
	form_class = PlaygroundForm
	success_url = "/playground/"

	def get_object(self, queryset=None):
		try:
			return Playground.objects.get(pk=self.kwargs['id'])
		except Playground.DoesNotExist:
			raise Http404

class PlaygroundListView(ListView):
	model = Playground
	template_name = 'playground_list.html'
	context_object_name = 'playground_list'

class PlaygroundDetailView(DetailView):
	template_name = 'playground_detail.html'
	context_object_name = 'playground'
	model = Playground
