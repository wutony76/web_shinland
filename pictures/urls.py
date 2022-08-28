from django.conf.urls.defaults import *

urlpatterns = patterns('pictures',
		url(r'^picture/(?P<id>\d+)/$', 'views.picture_response', name='picture'),
		url(r'^upload/$', 'views.picture_upload', name='upload'),
		url(r'^insert/$', 'views.picture_insert', name='insert'),
		url(r'^insertlist/$', 'views.picture_insertlist', name='insertlist'),
		url(r'^set/$', 'views.picture_set', name='picture_set'),
)
