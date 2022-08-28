from django.conf.urls.defaults import *

urlpatterns = patterns('contactus',
		url(r'^$', 'views.index', name='index'),
)
