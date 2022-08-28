from django.conf.urls.defaults import *

urlpatterns = patterns('album',
		url(r'^$', 'views.index', name='index'),
		url(r'^photolist/(?P<album_id>\d+)/$', 'views.photo_list', name='photo_list'),
		url(r'^photo/(?P<photo_id>\d+)/$', 'views.photo_response', name='photo'),
		url(r'^thumb/(?P<photo_id>\d+)/$', 'views.photo_thumb', name='photo_thumb'),
		url(r'^upload/(?P<album_id>\d+)/$', 'views.photo_upload', name='upload'),
		url(r'^photo_changelist/(?P<album_id>\d+)/$', 'views.photo_changelist', name='photo_changelist'),
		url(r'^coverreset/(?P<photo_id>\d+)/$', 'views.cover_reset', name='cover_reset'),
)
