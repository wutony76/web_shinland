from album.models import Album, Photo
from django.contrib import admin

class PhotoInline(admin.TabularInline):
	template = 'album/photo_inline.html'
	model = Photo
	exclude = ('author', 'weight')

class AlbumAdmin(admin.ModelAdmin):
	change_form_template = 'album/change_form.html'
	exclude = ('cover', 'slug', 'author')
	inlines = [PhotoInline]

	def has_delete_permission(self, request, obj=None):
		if obj and obj.slug:
			return False
		return super(AlbumAdmin, self).has_delete_permission(request, obj)

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.author = request.user
		obj.save()

	def save_formset(self, request, form, formset, change):

		for _form in formset:		
			if not _form.instance.description:
				upload_file = request.FILES.get('%s-image' % _form.prefix)
				if upload_file:
					_form.instance.description = upload_file.name
					_form.instance.save()


		formset.save()



admin.site.register(Album, AlbumAdmin)
