from django.conf.urls.defaults import *

urlpatterns = patterns('profiles',
		url(r'^photo/(?P<profile_id>\d+)/$', 'views.userphoto', name='photo'),
		url(r'^change/$', 'views.profile_change', name='profile_change'),
		url(r'^uploado/$', 'views.photo_upload', name='photo_upload'),
)
