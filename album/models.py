from lazy.models import ImageField
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Album(models.Model):
	author = models.ForeignKey(User, null=True)
	name = models.CharField(verbose_name=_('name'), max_length=50)
	slug = models.SlugField(unique=True, null=True, blank=True)
	weight = models.IntegerField(default=0)
	cover = models.ForeignKey('Photo', null=True, related_name='cover_set')
	description = models.CharField(verbose_name=_('description'), max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def cover_url(self):
		if self.cover:
			url = reverse('album:photo_thumb', args=[self.cover.id])
		else:
			url = '%simages/icon_folder.png' % settings.STATIC_URL

		return url

	def __unicode__(self):
		return self.name

class Photo(models.Model):
	author = models.ForeignKey(User, null=True)
	album = models.ForeignKey(Album, null=True, blank=True)
	weight = models.IntegerField(default=0)
	image = ImageField(auto_thumb=(800, 600), null=True)
	description = models.CharField(verbose_name=_('description'), max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
