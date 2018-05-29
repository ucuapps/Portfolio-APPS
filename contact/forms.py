from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=255, help_text='255 characters max.')
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)
