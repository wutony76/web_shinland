from profiles.models import Profile
from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'nickname')

admin.site.register(Profile, ProfileAdmin)
