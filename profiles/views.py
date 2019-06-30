from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model
from dal import autocomplete
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import date

from profiles.models import User, Interests
from student.views import student_login_required
from teacher.views import teacher_login_required
from student.views import SkillsAutocomplete

from student.models import Student
from .forms import UserForm
from .forms import SearchForm

from internships.models import Internship, Application


@login_required
def index(request):
    # template = 'profiles/index.html'
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
    # if u.is_teacher:
    #   context = dict(found_user=u, title="Teacher")
    #  return render(request, "teacher-inf.html", context)
    # else:
    context = dict(found_user=u, title="User")
    return render(request, "user.html", context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            users = User.objects.all()
            if form.cleaned_data['current_study_year']:
                users = users.filter(
                    student__current_study_year__icontains=form.cleaned_data['current_study_year'])
            if form.cleaned_data['last_name']:
                users = users.filter(last_name__icontains=form.cleaned_data['last_name'])
            if form.cleaned_data['first_name']:
                users = users.filter(first_name__icontains=form.cleaned_data['first_name'])
            # advanced search
            if form.cleaned_data['hard_skills']:
                users = users.filter(student__hard_skills=form.cleaned_data['hard_skills'])
            if form.cleaned_data['prog_lang']:
                users = users.filter(student__programming_languages=form.cleaned_data['prog_lang'])
            if form.cleaned_data['fields_of_interests']:
                users = users.filter(fields_of_interests=form.cleaned_data['fields_of_interests'])

            return render(request, 'search.html', {'form': form, 'users': users})
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})


def show_internships(request):
    internships = Internship.objects.all()
    if request.user.is_teacher:
        archive = list()
        actual_interns = list()
        for i in internships:
            if i.deadline < date.today():
                archive.append(i)
            else:
                actual_interns.append(i)
        return render(request, "internships.html",
                      {'internships': actual_interns, 'archive': archive, 'user': request.user})
    elif request.user.is_student:
        my_apps = Application.objects.filter(applicant=request.user.student)

        available_interns = internships
        my_interns = [app.internship for app in my_apps]
        available_interns = [intern for intern in available_interns if intern not in my_interns]

        return render(request, "internships.html", {'internships': available_interns, 'my_internships': my_interns})


class InterestsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Interests.objects.none()

        qs = Interests.objects.filter(interest_type="professional")

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs.all()


class HobbyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Interests.objects.none()

        qs = Interests.objects.filter(interest_type="hobby")

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs.all()
