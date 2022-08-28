import datetime
from pictures.models import Picture, PictureSet
from django.template import Library
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

register = Library()

@register.simple_tag
def picture_url_by_obj(obj, default_img=None):
	contenttype = ContentType.objects.get_for_model(obj)
	picsets = PictureSet.objects.filter(object_id=obj.id, content_type=contenttype)[:1]
	if picsets:
		picset = picsets[0]
		return reverse('pictures:picture', args=[picset.picture_id])

	if default_img:
		'%simages/%s' % (settings.STATIC_URL, default_img) 

	return '%simages/picture_default.jpg' % settings.STATIC_URL 
