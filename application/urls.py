from django.conf.urls import patterns, include, url
from application.views import create

urlpatterns = patterns('',
    url(r'^create', create),
)
