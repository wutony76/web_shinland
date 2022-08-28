import os
from django.core.management.base import BaseCommand, CommandError
from django.db import models
from django.utils._os import safe_join
from django.conf import settings

def get_filefields(model):
	fields = []
	for field in model._meta.fields:
		if issubclass(field.__class__, models.FileField):
			fields.append(field)
	return fields

class Command(BaseCommand):
	
	def handle(self, *args, **options):

		MEDIA_ROOT = safe_join(settings.MEDIA_ROOT)
		active_paths = []
		
		for app_mod in models.get_apps():
			for model in models.get_models(app_mod):
				filefields = get_filefields(model)			

				for field in filefields:					
					paths = [
							safe_join(MEDIA_ROOT, path)
							for path in list(model.objects.values_list(field.name, flat=True))
							]
					active_paths += paths

		for root, dirs, files in os.walk(MEDIA_ROOT):
			for filename in files:
				filepath = os.path.join(root, filename)
				if filepath not in active_paths:
					print 'remove', filepath
					os.remove(filepath)

