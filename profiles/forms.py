from django.utils.translation import ugettext_lazy as _
from django.forms import forms
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
