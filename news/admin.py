from news.forms import MediaInlineForm
from news.models import News, Category, Media
from pictures.models import Picture, PictureSet
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _

class MediaInline(admin.StackedInline):
	model = Media
	form = MediaInlineForm
	verbose_name = _('choice media')
	max_num = 1

class NewsAdmin(admin.ModelAdmin):
	exclude = ('author', 'weight')
	list_display = ('title', 'pub_date', )
	inlines = [MediaInline]

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.author = request.user
		obj.save()

admin.site.register(Category)
admin.site.register(News, NewsAdmin)
