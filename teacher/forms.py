from dal import autocomplete
from django import forms


from .models import Teacher, Subject


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ('user',)
        widgets = {
            'subjects': autocomplete.ModelSelect2Multiple(url='subjects-autocomplete'),}



