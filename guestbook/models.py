from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey(User, null=True, blank=True)
	body = models.CharField(max_length=2000)
	ipaddr = models.IPAddressField()
	pub_date = models.DateTimeField(auto_now_add=True)

class Reply(models.Model):
	post = models.ForeignKey(Post)
	author = models.ForeignKey(User)
	body = models.CharField(max_length=2000)
	pub_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-pub_date']
