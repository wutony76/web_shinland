from django.conf import settings

def static(request):
	data = {}
	host = request.get_host()
	#for dynamic domain names
	if host == u'www.bigpland.com':
		data['STATIC_URL'] = u'/shinland/static/'

	return data
