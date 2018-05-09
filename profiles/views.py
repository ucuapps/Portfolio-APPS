from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'profiles/index.html'
    return render(request, template, {})
