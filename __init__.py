from shinland import admin

"""
from django.contrib.auth.models import User, Group

admin.site.register(User)
admin.site.register(Group)
"""
import django
django.contrib.admin.site = admin.site
