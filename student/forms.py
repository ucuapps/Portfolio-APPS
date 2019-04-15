from django import forms
from django.forms import ClearableFileInput
from django.shortcuts import render

from review_request.forms import DateInput


from .models import Student, Project, WorkingExperience, VolunteerExperience, Language, Skill, Education, \
    ProgrammingLanguage

from django.utils.translation import ugettext_lazy as _

from dal import autocomplete

# ClearableFileInput.template_name = 'django_overrides/forms/widgets/clearable_file_input.html'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user', 'cv_soft_skills', 'cv_hard_skills', 'cv_programming_languages', 'cv_volunteering', \
                   'cv_working', 'cv_projects', 'cv_summary', 'cv_style',)
        widgets = {
            'soft_skills': autocomplete.ModelSelect2Multiple(url='soft-autocomplete'),
            'hard_skills': autocomplete.ModelSelect2Multiple(url='hard-autocomplete'),
            'programming_languages': autocomplete.ModelSelect2Multiple(url='planguage-autocomplete'),

        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        # self.fields["programming_languages"].queryset = ProgrammingLanguage.objects.filter(skill_type="programming")
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


class cvForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('cv_hard_skills', 'cv_soft_skills', 'cv_programming_languages',\
                  'cv_projects', 'cv_volunteering', 'cv_working', 'cv_summary', 'cv_style',)
        labels = {
            'cv_hard_skills': _('Hard skills:'),
            'cv_soft_skills': _('Soft skills:'),
            'cv_programming_languages': _('Programming languages:'),
            'cv_summary': _('Summary:'),
            'cv_projects': _('Projects:'),
            'cv_volunteering': _('Volunteering experience:'),
            'cv_working': _('Working experience:'),
            'cv_style': _('CV design:'),
        }
        widgets = {
            'cv_hard_skills': autocomplete.ModelSelect2Multiple(url='cv-hard-autocomplete'),
            'cv_soft_skills': autocomplete.ModelSelect2Multiple(url='cv-soft-autocomplete'),
            'cv_programming_languages': autocomplete.ModelSelect2Multiple(url='cv-plang-autocomplete'),
            'cv_projects': autocomplete.ModelSelect2Multiple(url='projects-autocomplete'),
            'cv_volunteering': autocomplete.ModelSelect2Multiple(url='volunteer-autocomplete'),
            'cv_working': autocomplete.ModelSelect2Multiple(url='working-autocomplete'),
            'cv_summary': forms.Textarea(attrs={'rows': 3}),

            'cv_style': autocomplete.ModelSelect2()
        }

        def __init__(self, *args, **kwargs):
            super(cvForm, self).__init__(*args, **kwargs)
            # self.fields["cv_programming_languages"].queryset = Skill.objects.filter(skill_type="programming")
            self.fields['cv_programming_languages'].queryset = Skill.objects.filter(skill_type="programming")
            self.fields["cv_soft_skills"].queryset = Skill.objects.filter(skill_type="soft")
            self.fields["cv_hard_skills"].queryset = Skill.objects.filter(skill_type="hard")
            self.fields["cv_projects"].queryset = Project.objects.filter(collaborators=self.request.user)
            self.fields["cv_volunteering"].queryset = VolunteerExperience.objects.filter(user=self.request.user)
            self.fields["cv_working"].queryset = WorkingExperience.objects.filter(user=self.request.user)
