from django.conf.urls import patterns, include, url
from django_playground.views import PlaygroundFormView
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^playground-form/$', PlaygroundFormView.as_view(), name='playground_form'),
    url(r'^form-success/$', TemplateView.as_view(template_name="success.html"), name="success"), 
    url(r'^admin/', include(admin.site.urls)),
)
