from django.conf.urls import patterns, include, url

from basic.views import sayhello

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', sayhello, name='home'),
)
