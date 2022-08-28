import os
from models import Download, Article, ArticleCategory, MIMETYPES
from django.contrib import admin

class ArticleCategoryAdmin(admin.ModelAdmin):
	exclude = ('parent', 'weight')


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date')
	exclude = ('author', 'weight')

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.author = request.user
		obj.save()

class DownloadAdmin(admin.ModelAdmin):

	list_display = ('title', 'pub_date')
	exclude = ('author', 'mimetype', 'ext')

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.author = request.user

		upload_file = request.FILES.get('file')
		if upload_file:
			name, ext = os.path.splitext(upload_file.name)
			ext = ext.strip('.')
			obj.ext = ext
			obj.mimetype = MIMETYPES.get(ext.lower(), None)
			if not obj.title:
				obj.title = name
		obj.save()

admin.site.register(Download, DownloadAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

