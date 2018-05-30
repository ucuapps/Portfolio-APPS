from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model
from dal import autocomplete
from django.contrib.auth.decorators import login_required, user_passes_test


from student.models import Student
from .forms import UserForm

@login_required
def index(request):
    template = 'profiles/index.html'
    # return render(request, template, {})
    # if request.user.is_authenticated:
    return redirect('show-user', request.user.id)
    # return render(request, template, {})


def about(request):
    template = 'profiles/about.html'
    return render(request, template, {})


def edit_user(request):
    template = "edit/user.html"
    context = {}

    if request.method == "POST":
        form = UserForm(request.POST or None, request.FILES, instance=request.user)
    else:
        form = UserForm(instance=request.user)
    print(request.user.email, request.user.first_name)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your data has been edited.")
    context["form"] = form
    print(form)
    return render(request, template, context)


class UsersAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return get_user_model().objects.none()

        qs = get_user_model().objects

        if self.q:
            qs = qs.filter(email__istartswith=self.q)

        return qs.all()


@login_required
def show_user(request, pk):
    u = get_object_or_404(get_user_model(), id=pk)
    context = dict(found_user=u, title="User")
    return render(request, "user.html", context)
