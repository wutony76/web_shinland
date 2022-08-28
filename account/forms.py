from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class AuthenticateForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField( max_length=30, widget=forms.PasswordInput)
	remember = forms.BooleanField(label=_('remember'), required=False)

class SignupForm(forms.Form):
	username = forms.CharField(label=_('username'), min_length=5, max_length=30)
	email = forms.EmailField(label=_('email'))
	password = forms.CharField(label=_('password'), max_length=30, widget=forms.PasswordInput)
	password_confirm = forms.CharField(label=_('Confirm your password'), max_length=30, widget=forms.PasswordInput)

	not_available_username = ('administrator', 'admin', 'root')

	def clean_username(self):
		username = self.cleaned_data['username']

		if username in self.not_available_username:
			raise forms.ValidationError(_("This username is illegal."))

		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username

		raise forms.ValidationError(_("A user with that username already exists."))

	def clean_password_confirm(self):
		password = self.cleaned_data.get('password') 
		password_confirm = self.cleaned_data.get('password_confirm') 
		if password != password_confirm:
			raise forms.ValidationError(_("The two password fields didn't match."))

		return password_confirm

	def save(self):
		username = self.cleaned_data['username']
		email = self.cleaned_data['email']
		password = self.cleaned_data.get('password')

		user = User.objects.create_user(username, email, password)


class OpenIDRegistrationForm(forms.Form):
	username = forms.CharField(label='username', max_length=30)

	def __init__(self, *args, **kwargs):
		#registration consumer do_register
		self.openid = kwargs.pop('openid', None)
		reserved_usernames = kwargs.pop('reserved_usernames', [])
		no_duplicate_emails = kwargs.pop('no_duplicate_emails', False)

		super(OpenIDRegistrationForm, self).__init__(*args, **kwargs)
