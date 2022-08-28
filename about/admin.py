from about.models import About, Category
from pictures.admin import PictureSetInline
from pictures.widgets import WysiwygWidget
from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.generic import GenericStackedInline

class AboutAdmin(admin.ModelAdmin):
	list_display = ('title', 'category',)
	exclude = ('slug',)
	inlines = [PictureSetInline]
	formfield_overrides = {
			models.TextField: {'widget': WysiwygWidget}
	}

	def has_delete_permission(self, request, obj=None):
		if obj and obj.slug:
			return False
		return super(AboutAdmin, self).has_delete_permission(request, obj)

	def save_model(self, request, obj, form, change):
	
		obj.save()

admin.site.register(Category)
admin.site.register(About, AboutAdmin)
