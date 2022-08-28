from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^detail/(?P<id>\d+)', views.detail, name='detail')
		)
