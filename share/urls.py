from django.conf.urls.defaults import *

urlpatterns = patterns('share',
		url(r'^$', 'views.index', name='index'),
		url(r'^article/$', 'views.article_index', name='article_index'),
		url(r'^download/$', 'views.download_list', name='download_list'),
		url(r'^download/(?P<obj_id>\w+)/$', 'views.download', name='download'),
)
