from django import forms

from dal import autocomplete

from .models import Internship

class CreateInternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        exclude = ('created_by',)

    def __init__(self, *args, **kwargs):
        super(CreateInternshipForm, self).__init__(*args, **kwargs)