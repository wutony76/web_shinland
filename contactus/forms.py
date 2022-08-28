from django import forms
from models import Contactus

class ContactusForm(forms.Form):
	title = forms.CharField()
	body = forms.CharField(widget=forms.Textarea)
	email = forms.EmailField()

