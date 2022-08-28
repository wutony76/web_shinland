from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

admin_urlpatterns, app_name, namespace = admin.site.urls

urlpatterns = patterns('admin',
		url(r'^list_filter_toggle/$', 'views.list_filter_toggle', name='list_filter_toggle'),
) + admin_urlpatterns
