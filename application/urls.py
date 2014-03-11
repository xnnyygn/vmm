from django.conf.urls import patterns, include, url
from application import views

urlpatterns = patterns('',
    url(r'^create', views.create),
    url(r'^save', views.save),
    url(r'^list', views.list),
)
