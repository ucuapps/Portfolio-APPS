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


# class CustomClearableFileInputWidget(f.ClearableFileInput):
#     template_name = 'django_overrides/forms/widgets/clearable_file_input.html'


f.ClearableFileInput.template_name = 'django_overrides/forms/widgets/clearable_file_input.html'


class UserForm(f.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_image', 'first_name', 'last_name', 'mobile_number', 'git_link', 'fb_link',
                  'fields_of_interests')
        labels = {
            'git_link': _('Github link:'),
            'fb_link': _('Facebook link:'),
        }
        widgets = {
            'fields_of_interests': autocomplete.ModelSelect2Multiple(url='interests-autocomplete'),}


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


class SearchForm(f.Form):
    first_name= f.CharField(max_length=30, required=False,widget=f.TextInput(attrs={'placeholder': 'First name'}))
    last_name = f.CharField(max_length=30, required=False,
                                 widget=f.TextInput(attrs={'placeholder': 'Last name'}))
    current_study_year = f.IntegerField(required=False, initial=1)

    #language = f.ModelChoiceField(required=False,
                                #queryset=Language.objects.all(),
                                #widget=autocomplete.ModelSelect2Multiple(url='language-autocomplete')
                                #)


    #skills = f.ModelChoiceField(required=False,
    #    queryset=Skill.objects.all(),
    #    widget=autocomplete.ModelSelect2Multiple(url='skills-autocomplete')
    #)

   # fields_of_interests = f.ModelChoiceField(required=False,
    #                            queryset=Interests.objects.all(),
     #                           widget=autocomplete.ModelSelect2Multiple(url='interests-autocomplete')
      #                          )



    def clean_current_study_year(self):
        data = self.cleaned_data['current_study_year']

        if 1>data or data>4:
            raise ValidationError(_('Invalid current study year, try int between 1 and 4'))

        return data
