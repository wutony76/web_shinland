import os
from profiles.fields import ProfilePhotoField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

def photo_upload_to(model, filename):
	name, ext = os.path.splitext(filename)
	return 'profilephoto/%s%s' % (model.id, ext)


class Profile(models.Model):

	GENDERS = (
			('M', _('Male')),
			('F', _('Female')),
			)
		
	user = models.ForeignKey(User, unique=True)
	nickname = models.CharField(verbose_name=_('nickname'), max_length=50, null=True, blank=True)
	gender = models.CharField(verbose_name=_('gender'), choices=GENDERS, max_length=1, null=True, blank=True)
	birthday = models.DateField(verbose_name=_('birthday'), null=True, blank=True)
	website = models.URLField(verbose_name=_('website'), null=True, blank=True)
	photo = ProfilePhotoField(verbose_name=_('photo'), upload_to=photo_upload_to, null=True, blank=True)
	about = models.TextField(verbose_name=_('about'), null=True, blank=True)

	class Meta:
		db_table = 'profiles'
		verbose_name = _('profile')


def create_profile(sender, instance=None, **kwargs):
	if instance is None:
		return
	profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)
