import os
import math
import cStringIO
import uuid
from PIL import Image
from django.db.models.fields.files import ImageFieldFile as BaseImageFieldFile
from django.core.files.base import ContentFile
from django.db import models

class ImageFieldFile(BaseImageFieldFile):

	def save(self, name, content, save=True):

		if self.field.auto_thumb:
			img = Image.open(content)

			max_w, max_h = self.field.auto_thumb
			w, h = img.size
			w, h = float(w), float(h)

			if w > max_w or h > max_h:			
				
				rate = max(max_w/w, max_h/h)			
				scale = (int(math.ceil(w*rate)), int(math.ceil(h*rate)))

				img.thumbnail(scale, Image.ANTIALIAS)
				img  = img.crop((0, 0, max_w, max_h))
				buf = cStringIO.StringIO()
				img.save(buf, 'JPEG')
				#img.save(buf, img.format.upper())
				content = ContentFile(buf.getvalue())

		super(ImageFieldFile, self).save(name, content, save)


def generate_thumb(content, size):
	content.seek(0)
	max_w, max_h = size
	img = Image.open(content)
	w, h = img.size
	w, h = float(w), float(h)

	if w > max_w or h > max_h:			
		
		rate = max(max_w/w, max_h/h)			
		scale = (int(math.ceil(w*rate)), int(math.ceil(h*rate)))

		img.thumbnail(scale, Image.ANTIALIAS)
		img  = img.crop((0, 0, max_w, max_h))
		
	return img


def _default_upload_to(model, filename):
	opts = model._meta
	name, ext = os.path.splitext(filename)
	path = 'upload/%s_%s/%s%s' % (opts.app_label, opts.module_name, uuid.uuid1(), ext)
	print '_default_upload_to', path
	return path

class ImageField(models.ImageField):
	attr_class = ImageFieldFile

	def __init__(self, *args, **kwargs):
		self.auto_thumb = kwargs.pop('auto_thumb', None)
		if not kwargs.has_key('upload_to'):
			kwargs['upload_to'] = _default_upload_to
		return super(ImageField, self).__init__(*args, **kwargs)
