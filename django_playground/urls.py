from django.conf.urls import patterns, include, url
from django_playground.views import PlaygroundCreateView, PlaygroundUpdateView, PlaygroundListView, PlaygroundDetailView
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^playground/$', PlaygroundListView.as_view(), name="playground_list"),
    url(r'^playground/(?P<pk>\d+)/$', PlaygroundDetailView.as_view(), name="playground_detail"),
    url(r'^playground/create/$', PlaygroundCreateView.as_view(), name='playground_create'),
    url(r'^playground/(?P<id>\d+)/update/$', PlaygroundUpdateView.as_view(), name="playground_update"),
    url(r'^form-success/$', TemplateView.as_view(template_name="django_playground/success.html"), name="success"), 
    url(r'^admin/', include(admin.site.urls)),
)
