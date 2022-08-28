from models import Post
from django import forms

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('body',)

class BodyForm(forms.Form):
	body = forms.CharField()
