from django import forms
from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
		('zh-tw', _('Traditional Chinese')),
		('en-us', _('English')),
)


class LanguageSetForm(forms.Form):

	language = forms.ChoiceField(label=_('Language'), choices=LANGUAGES)

