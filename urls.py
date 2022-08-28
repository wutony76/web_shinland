from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
		url(r'^$', 'views.index', name='index'),
		url(r'^home/$', 'views.home', name='home'),
		url(r'^calendar/$', 'views.calendar_view', name='calendar'),
)

urlpatterns += patterns('',
		url(r'^about/', include('about.urls', namespace='about')),
		url(r'^accounts/', include('account.urls')),
		url(r'^admin/', include('admin.urls', app_name='admin', namespace='admin')),
		url(r'^album/', include('album.urls', namespace='album')),
		url(r'^contactus/', include('contactus.urls', namespace='contactus')),
		url(r'^calendar/', include('gcalendar.urls', namespace='gcalendar')),
		url(r'^guestbook/', include('guestbook.urls', namespace='guestbook')),
		url(r'^language/', include('language.urls')),
		url(r'^pictures/', include('pictures.urls', namespace='pictures')),
		url(r'^profile/', include('profiles.urls', namespace='profiles')),
		url(r'^news/', include('news.urls', namespace='news')),
		url(r'^share/', include('share.urls', namespace='share')),
)

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static('/static/', document_root=settings.STATIC_ROOT)
