import datetime
from pictures.models import Picture
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name	

class News(models.Model):
	author = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	weight = models.IntegerField(default=0)
	is_top = models.BooleanField(verbose_name=_('top'), default=False)
	title = models.CharField(verbose_name=_('title'), max_length=100)
	body = models.TextField(verbose_name=_('body'), null=True, blank=True)
	pub_date = models.DateTimeField(verbose_name=_('publish date'), default=datetime.datetime.now)
	date_modifiled = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True)

class Media(models.Model):
	news = models.ForeignKey(News)
	youtube = models.URLField(null=True, blank=True)
	picture = models.ForeignKey(Picture, null=True, blank=True)

	class Meta:
		unique_together = ('news',)

