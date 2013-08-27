from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
from . import views

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.entry),
    url(r'^thanks/', views.thanks),
    url(r'^confirm/(?P<key>[\w]{32})/$', views.confirm_entry, name='confirm_entry'),
)
