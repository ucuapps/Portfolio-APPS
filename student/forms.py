from django import forms
from django.forms import ClearableFileInput
from django.shortcuts import render

from review_request.forms import DateInput


from .models import Student, Project, WorkingExperience, VolunteerExperience, Language, Skill, Education


from dal import autocomplete

# ClearableFileInput.template_name = 'django_overrides/forms/widgets/clearable_file_input.html'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user', )
        widgets = {
            'soft_skills': autocomplete.ModelSelect2Multiple(url='soft-autocomplete'),
            'hard_skills': autocomplete.ModelSelect2Multiple(url='hard-autocomplete'),
            'programming_languages': autocomplete.ModelSelect2Multiple(url='planguage-autocomplete'),
            'hobbies': autocomplete.ModelSelect2Multiple(url='hobbies-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields["programming_languages"].queryset = Skill.objects.filter(skill_type="programming")
        self.fields["soft_skills"].queryset = Skill.objects.filter(skill_type="soft")
        self.fields["hard_skills"].queryset = Skill.objects.filter(skill_type="hard")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('__all__')
        widgets = {
            'technologies': autocomplete.ModelSelect2Multiple(url='planguage-autocomplete'),
            'collaborators': autocomplete.ModelSelect2Multiple(url='users-autocomplete'),
        }

        #
    # def __init__(self, *args, **kwargs):
    #     super(ProjectForm, self).__init__(*args, **kwargs)
    #     # self.fields["collaborators"].widget = forms.widgets.CheckboxSelectMultiple()


class WorkingExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkingExperience
        exclude = ('user',)
        widgets = {
            'period_start': DateInput(),
            'period_end': DateInput(),

        }


class VolunteerExperienceForm(forms.ModelForm):
    class Meta:
        model = VolunteerExperience
        exclude = ('user',)


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        exclude = ('user',)

class StudentSearch(forms.ModelForm):
  pass

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ('user',)
        widgets = {
            'period_start': DateInput(),
            'period_end': DateInput(),

        }
