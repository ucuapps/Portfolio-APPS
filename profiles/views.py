from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    template = 'profiles/index.html'
    return render(request, template, {})


def about(request):
    template = 'profiles/about.html'
    return render(request, template, {})
