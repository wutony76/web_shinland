from django.conf import settings
from django.middleware.locale import LocaleMiddleware as LocaleMiddlewareBase
from django.utils import translation

class LocaleMiddleware(LocaleMiddlewareBase):

	def process_request(self, request):
		try:

			language = request.session.get('django_language', None)
			if not language:
				#for ie error
				language = request.META.get('HTTP_ACCEPT_LANGUAGE', settings.LANGUAGE_CODE).split(',')[0]

			translation.activate(language)
			request.LANGUAGE_CODE = language

		except:
			pass
