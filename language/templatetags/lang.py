from language.forms import LanguageSetForm
from django.conf import settings
from django.template import Library
from django.template.loader import render_to_string
from django.middleware.csrf import get_token

register = Library()

@register.simple_tag(takes_context=True)
def lang_form(context):

	request = context['request']
	if hasattr(request, 'LANGUAGE_CODE'):
		language_code = request.LANGUAGE_CODE
	else:
		language_code = settings.LANGUAGE_CODE

	form = LanguageSetForm(initial={'language': language_code})

	return render_to_string('language/lang_form.html', {
		'csrf_token': get_token(request),
		'form': form,
		'next': request.get_full_path(),
		})
