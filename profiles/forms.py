from django.utils.translation import ugettext_lazy as _
from django.forms import forms
from django import forms as f
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.helpers import ImmediateHttpResponse
from django.http import Http404, HttpResponse


class DomainCheckAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        email = super().clean_email(email)
        if email.split('@')[1].lower() != "ucu.edu.ua":
            raise forms.ValidationError("Your domain is bad.")
        return email


class SocialDomainCheckAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        u = sociallogin.user
        if not u.email.split('@')[1] == "ucu.edu.ua":
            raise ImmediateHttpResponse(HttpResponse("It is not allowed"))
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
