from django import forms

from dal import autocomplete

from .models import Internship, Application


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateInternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        exclude = ('created_by', 'applicants', 'approved_applicants')
        widgets = {
            'deadline': DateInput(),
            'is_inner': forms.CheckboxInput(attrs={'id': 'inner_check'})
        }
        labels = {
            'is_inner': "Is it an inner internship?"
        }

    def __init__(self, *args, **kwargs):
        super(CreateInternshipForm, self).__init__(*args, **kwargs)


class ApplyToInternshipForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('internship', 'applicant', 'sent',)
        labels = {
            'cv': 'CV',
        }

    def __init__(self, *args, **kwargs):
        super(ApplyToInternshipForm, self).__init__(*args, **kwargs)
