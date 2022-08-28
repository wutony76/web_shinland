from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin


class UserAdmin(BaseUserAdmin):
	filter_horizontal = ('user_permissions', 'groups')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

