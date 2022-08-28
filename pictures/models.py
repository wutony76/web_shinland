import os
from lazy.models import ImageField
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey


def upload_to(model, filename):
	import uuid
	name, ext = os.path.splitext(filename)
	return 'upload/%s%s' % (uuid.uuid1(), ext)

class Picture(models.Model):
	author = models.ForeignKey(User)
	image = ImageField(auto_thumb=(800, 600))
	description = models.CharField(max_length=1000, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)


class PictureSet(models.Model):
	picture = models.ForeignKey(Picture)
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey()
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = (('picture', 'content_type', 'object_id'))
