from django.views.decorators.cache import never_cache
from django.contrib.admin.sites import AdminSite as BaseAdminSite
from account import views as act_view

class AdminSite(BaseAdminSite):

	login_template = 'registration/login.html'

site = AdminSite()
