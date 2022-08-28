from pictures.models import Picture, PictureSet
from pictures.widgets import PictureSetWidget
from django import forms


class PictureChoiceField(forms.IntegerField):
	widget = PictureSetWidget

	def to_python(self, value):
		print 'to_python', value

		if value:
			return Picture.objects.get(id=value)

class PictureSetInlineForm(forms.ModelForm):
	picture = PictureChoiceField(required=False, widget=PictureSetWidget(can_remove=False))
	class Meta:
		model = PictureSet

