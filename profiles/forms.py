from dal import autocomplete
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect
from django.forms import forms, ChoiceField, CheckboxInput, BooleanField
from django import forms as f
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.helpers import ImmediateHttpResponse
from django.http import Http404, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.conf import settings
from django.core.exceptions import ValidationError

from profiles.models import Interests
from student.models import Skill, Language

from django.db import models

# class IntegerRangeField(models.IntegerField):
#     def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
#         self.min_value, self.max_value = min_value, max_value
#         models.IntegerField.__init__(self, verbose_name, name, **kwargs)
#
#     def formfield(self, **kwargs):
#         defaults = {'min_value': self.min_value, 'max_value': self.max_value}
#         defaults.update(kwargs)
#         return super(IntegerRangeField, self).formfield(**defaults)


# class CustomClearableFileInputWidget(f.ClearableFileInput):
#     template_name = 'django_overrides/forms/widgets/clearable_file_input.html'


f.ClearableFileInput.template_name = 'django_overrides/forms/widgets/clearable_file_input.html'


class UserForm(f.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_image', 'first_name', 'last_name', 'mobile_number', 'git_link', 'fb_link',
                  'fields_of_interests', 'hobbies')
        labels = {
            'git_link': _('Github link:'),
            'fb_link': _('Facebook link:'),
        }
        widgets = {
            'fields_of_interests': autocomplete.ModelSelect2Multiple(url='interests-autocomplete'),
            'hobbies': autocomplete.ModelSelect2Multiple(url='hobby-autocomplete')
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["fields_of_interests"].queryset = Interests.objects.filter(interest_type="professional")
        self.fields["hobbies"].queryset = Interests.objects.filter(interest_type="hobby")


class DomainCheckAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        """
        Checks whether or not the site is open for signups.

        Next to simply returning True/False you can also intervene the
        regular flow by raising an ImmediateHttpResponse

        (Comment reproduced from the overridden method.)
        """
        return False

    def clean_email(self, email):
        email = super().clean_email(email)
        email_domain = email.split('@')[1].lower()
        if email_domain != "ucu.edu.ua" and email not in ("kuservol3@gmail.com"):
            raise forms.ValidationError("Your domain is bad.")
        return email


class SocialDomainCheckAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, *args, **kwargs):
        """
        Checks whether or not the site is open for signups.

        Next to simply returning True/False you can also intervene the
        regular flow by raising an ImmediateHttpResponse

        (Comment reproduced from the overridden method.)
        :param **kwargs:
        """
        return True

    def pre_social_login(self, request, sociallogin):
        u = sociallogin.user
        email = u.email
        email_domain = email.split('@')[1].lower()
        if email_domain != "ucu.edu.ua" and email not in ("kuservol3@gmail.com"):
            messages.error(request, "Only @ucu.edu.ua domains are allowed, but yours is %s (%s)" % (
                u.email.split("@")[1], u.email))
            raise ImmediateHttpResponse(redirect('account_signup'))
        # if get_user_model().objects.filter(email=u.email).exists():
        #     raise ImmediateHttpResponse(HttpResponse("User with such email exists"))
        return super().pre_social_login(request, sociallogin)


class CustomSignupForm(f.Form):
    first_name = f.CharField(max_length=30, label='First name',
                             widget=f.TextInput(attrs={'placeholder': 'Your first name'}))
    last_name = f.CharField(max_length=30, label='Last name',
                            widget=f.TextInput(attrs={'placeholder': 'Your last name'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


from django.core.validators import MaxValueValidator, MinValueValidator


class SearchForm(f.Form):
    first_name = f.CharField(max_length=30, required=False, widget=f.TextInput(attrs={'placeholder': 'First name'}))
    last_name = f.CharField(max_length=30, required=False,
                            widget=f.TextInput(attrs={'placeholder': 'Last name'}))
    current_study_year = f.IntegerField(required=False, initial=1,
                                        validators=[
                                            MaxValueValidator(4),
                                            MinValueValidator(1)
                                        ])

    hard_skills = f.ModelChoiceField(required=False,
                                     queryset=Skill.objects.all(),
                                     widget=autocomplete.ModelSelect2(url='hard-autocomplete'),
                                     help_text="Hard skill")

    prog_lang = f.ModelChoiceField(required=False,
                                   queryset=Skill.objects.all(),
                                   widget=autocomplete.ModelSelect2(url='planguage-autocomplete'),
                                   help_text="Programming language")

    fields_of_interests = f.ModelChoiceField(required=False,
                                             queryset=Interests.objects.all(),
                                             widget=autocomplete.ModelSelect2(url='interests-autocomplete'),
                                             help_text="Field of professional interests")

    def clean_current_study_year(self):
        if self.cleaned_data['current_study_year']:
            data = self.cleaned_data['current_study_year']
            if 1 > data or data > 4:
                raise ValidationError(_('Invalid current study year, try int between 1 and 4'))
            return data
