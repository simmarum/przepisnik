from django import forms
from django.utils.translation import ugettext


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = ugettext("Your name:")
        self.fields['contact_email'].label = ugettext("Your email:")
        self.fields['content'].label = ugettext("What do you want to say?")
