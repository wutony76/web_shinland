from models import Picture, PictureSet
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.generic import GenericStackedInline
from django.utils.translation import ugettext_lazy as _

class PictureAdmin(admin.ModelAdmin):

	exclude = ('author',)
	list_display = ('picture',)

	def picture(self, obj):
		return '<img src="%s?w=100&h=100">' % reverse('pictures:picture', args=[obj.id])

	picture.allow_tags = True

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.author = request.user
		obj.save()



class PictureSetAdmin(admin.ModelAdmin):
	pass

admin.site.register(Picture, PictureAdmin)
admin.site.register(PictureSet, PictureSetAdmin)

from forms import PictureSetInlineForm

class PictureSetInline(GenericStackedInline):
	model = PictureSet
	form = PictureSetInlineForm
	verbose_name = _('related pictures')
	extra = 1
