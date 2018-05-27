from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages

from .forms import UserForm


def index(request):
    template = 'profiles/index.html'
    return render(request, template, {})


def about(request):
    template = 'profiles/about.html'
    return render(request, template, {})


def edit_user(request):
    template = "edit/user.html"
    context = {}

    form = UserForm(request.POST or None, request.FILES, instance=request.user)
    if request.POST and form.is_valid():
        form.save()
        messages.success(request, "Your data has been edited.")
    context["form"] = form
    return render(request, template, context)
