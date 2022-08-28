import os
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class ArticleCategory(models.Model):
	weight = models.IntegerField(default=0)
	name = models.CharField(max_length=30)
	parent = models.ForeignKey('self', null=True, blank=True)

	def __unicode__(self):
		return self.name

class Article(models.Model):
	author = models.ForeignKey(User)
	category = models.ForeignKey(ArticleCategory, null=True, blank=True)
	weight = models.IntegerField(default=0)
	title = models.CharField(max_length=100)
	body = models.TextField()
	modified_date = models.DateTimeField(auto_now=True)
	pub_date = models.DateTimeField(auto_now_add=True)


MIMETYPES = {
		'jpg': 'image/jpeg',
		'jpeg': 'image/jpeg',
		'bmp': 'image/bmp',
		'png': 'image/png',
		'gif': 'image/gif',
		'tiff': 'image/tiff',
		'doc': 'application/msword',
}

def upload_to(model, filename):

	return 'download/%s' % uuid.uuid1()

class Download(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=100, null=True, blank=True)
	file = models.FileField(upload_to=upload_to)
	mimetype = models.CharField(max_length=30, null=True)
	ext = models.CharField(max_length=10, null=True)
	pub_date = models.DateTimeField(auto_now_add=True)
