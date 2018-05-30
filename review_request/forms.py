from django import forms

from dal import autocomplete

from .models import ReviewRequest
from student.models import Skill


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

    def __init__(self, *args, **kwargs):
        super(ReviewRequestForm, self).__init__(*args, **kwargs)
        self.fields["skills"].queryset = Skill.objects.all()
