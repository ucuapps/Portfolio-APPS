from django import forms

from dal import autocomplete

from .models import ReviewRequest
class DateInput(forms.DateInput):
    input_type = 'date'

class ReviewRequestForm(forms.ModelForm):
    class Meta:
        model = ReviewRequest
        exclude = ('student', 'teacher', 'accepted',)
        widgets = {
            'deadline': DateInput(),
            'skills': autocomplete.ModelSelect2Multiple(url='skills-autocomplete'),
        }