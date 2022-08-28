from news.models import Media
from pictures.forms import PictureChoiceField
from django import forms


class MediaInlineForm(forms.ModelForm):
	picture = PictureChoiceField(required=False)
	class Meta:
		model =  Media
