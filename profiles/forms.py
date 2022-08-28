from profiles.models import Profile
from django import forms
from django.contrib.auth.models import User

class ProfileChangeForm(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = ('user', 'photo')

class UserChangeForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('last_name', 'first_name', 'email')
