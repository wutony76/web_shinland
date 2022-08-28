from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('about',
		url(r'^$', 'views.index', name='index'),
		url(r'^environ/$', 'views.environ', name='environ'),
		url(r'^traffic/$', 'views.traffic', name='traffic'),
		url(r'^course/$', 'views.course', name='course'),
		url(r'^page/(?P<about_id>\d+)/$', 'views.page_view', name='page'),
		url(r'^teacher/$', 'views.teacher_list', name='teacher_list'),
		url(r'^teacher/(?P<user_id>\d+)/$', 'views.teacher_view', name='teacher'),
)
