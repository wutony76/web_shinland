import datetime
from pictures.models import Picture, PictureSet
from django.template import Library
from album.models import Album, Photo
from django.conf import settings
from django.core.urlresolvers import reverse

register = Library()

@register.simple_tag
def album_thumb_by_obj(obj, default_img=None):
	url = ''

	if isinstance(obj, Album):
		pic = obj.cover

		if not pic:
			pics = obj.photo_set.all()[:1]
			if pics:
				pic = pics[0]

		if not pic:
			return '%simages/%s' % (settings.STATIC_URL, default_img)

		url = reverse('album:photo_thumb', args=[pic.id])

	return url
