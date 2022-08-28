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

		img = Image.open(content)

		max_w, max_h = (200, 200)
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

class ProfilePhotoField(models.ImageField):
	attr_class = ImageFieldFile
