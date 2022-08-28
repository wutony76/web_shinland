from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^setlang/$', 'django.views.i18n.set_language', name='setlang'),
)
