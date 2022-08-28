from django.db import models

class Contactus(models.Model):
	title = models.CharField(max_length=100, null=True)
	body = models.TextField()
	mail = models.EmailField()
	date = models.DateTimeField(auto_now_add=True)
