from profiles.models import Profile
from django.template import Library
from django.conf import settings
from django.core.urlresolvers import reverse

register = Library()

@register.simple_tag(takes_context=True)
def fullname(context, user):
	language_code = context.get('LANGUAGE_CODE', 'zh-tw')
	if language_code == 'zh-tw':
		return '%s %s' % (user.last_name, user.first_name)

	return '%s %s' % (user.first_name, user.last_name)


@register.simple_tag
def userphoto(obj):
	url = None
	try:
		if isinstance(obj, Profile):
			profile = obj
		else:
			#is user
			profile = obj.get_profile()

		if profile.photo:
			url = reverse('profiles:photo', args=[profile.id])
	except:
		pass

	if url is None:
		url = '%simages/userphoto_default.png' % settings.STATIC_URL 

	return '<img src="%s" />' % url


