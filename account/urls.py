from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
		url(r'^$', 'account.views.index', name='auth_index'),
		#base auth views
		url(r'^login/$', auth_views.login, {
			'template_name': 'registration/login.html'
			}, name='auth_login'),
		url(r'^logout/$', auth_views.logout, {
			'template_name': 'registration/logout.html'
			}, name='auth_logout'),
		url(r'^password_change/$', auth_views.password_change, {
			}, name='password_change'),
		url(r'^password_change_done/$', auth_views.password_change_done, {
			}, name='password_change_done'),
		url(r'^signup/$', 'account.views.signup', name='auth_signup'),
)
