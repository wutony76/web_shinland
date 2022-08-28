from pictures.models import PictureSet
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.generic import GenericRelation
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
	parent = models.ForeignKey('self', null=True, blank=True)
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

class About(models.Model):
	category = models.ForeignKey(Category, verbose_name=_('category'), null=True, blank=True)
	slug = models.SlugField(unique=True, null=True, blank=True)
	title = models.CharField(verbose_name=_('title'), max_length=100)
	body = models.TextField(verbose_name=_('content'), null=True, blank=True)
	date_modifiled = models.DateTimeField(verbose_name=_('image'), auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True)

	picture_sets = GenericRelation(PictureSet)
