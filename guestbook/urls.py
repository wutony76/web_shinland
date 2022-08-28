from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('guestbook',
    url(r'^$', 'views.index', name='index'),
    url(r'^add/$', 'views.post_add', name='post_add'),
    url(r'^detail/(?P<obj_id>\d+)/$', 'views.post_detail', name='post_detail'),
    url(r'^reply/(?P<obj_id>\d+)/$', 'views.post_reply', name='post_reply'),
)
