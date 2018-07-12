from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from student.models import Student
from student.forms import StudentSearch

from .forms import StudentForm, ProjectForm, WorkingExperienceForm, VolunteerExperienceForm, LanguageForm, EducationForm
from .models import Project, WorkingExperience, VolunteerExperience, Language, Skill, Education


from weasyprint import HTML, CSS
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.conf import settings
import os
#import pdfkit


student_login_required = user_passes_test(lambda u: u.is_student, login_url='/')


def user_login_required(view_func):
    decorated_view_funct = login_required(student_login_required(view_func))
    return decorated_view_funct


@student_login_required
def edit_student(request):
    template = "edit/student.html"
    context = {}

    if request.method == "POST":
        form = StudentForm(request.POST, instance=request.user.student)
    else:
        form = StudentForm(instance=request.user.student)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your profile data has been changed")
    context["form"] = form
    context["languages"] = Language.objects.filter(user=request.user)
    return render(request, template, context)

@user_login_required
def edit_project(request, pk=None):
    if pk:
        title = 'Edit project:'
        project = get_object_or_404(Project, pk=pk)
        if request.user not in project.collaborators.all():
            return HttpResponseForbidden()
    else:
        title = 'Create project:'
        project = Project()

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
    else:
        form = ProjectForm(instance=project)

    if request.method == "POST" and form.is_valid():
        project = form.save()
        project.collaborators.add(request.user)
        project.save()

        messages.success(request, "Process finished successfully")
        return redirect('edit_projects')

    return render(request, template_name='edit/project.html', context={'form': form, 'title': title})

@user_login_required
def edit_projects(request):
    projects = Project.objects.filter(collaborators=request.user).distinct()
    return render(request, 'edit/projects.html', context={'projects': projects, 'title': "Projects"})

@user_login_required
def edit_work_exp(request, pk=None):
    if pk:
        title = 'Edit working experience:'
        we = get_object_or_404(WorkingExperience, pk=pk)
        if request.user != we.user:
            return HttpResponseForbidden()
    else:
        title = 'Create working experience:'
        we = WorkingExperience()

    # form = WorkingExperienceForm(request.POST or None, instance=we)
    if request.method == "POST":
        form = WorkingExperienceForm(request.POST, instance=we)
    else:
        form = WorkingExperienceForm(instance=we)

    if request.method == "POST" and form.is_valid():
        we = form.save(commit=False)
        we.user = request.user
        we.save()

        messages.success(request, "Process finished successfully")
        return redirect('edit_work_exps')

    return render(request, template_name='edit/work_experience.html', context={'form': form, 'title': title})

@user_login_required
def edit_work_exps(request):
    work_exps = WorkingExperience.objects.filter(user=request.user)
    return render(request, 'edit/work_experiences.html', {'work_exps': work_exps, 'title': 'Working experiences'})

@user_login_required
def edit_volunteer_exp(request, pk=None):
    if pk:
        title = 'Edit volunteer experience:'
        ve = get_object_or_404(VolunteerExperience, pk=pk)
        if request.user != ve.user:
            return HttpResponseForbidden()
    else:
        title = 'Create volunteer experience:'
        ve = VolunteerExperience()
        ve.user = request.user

    # form = VolunteerExperienceForm(request.POST or None, instance=ve)
    if request.method == "POST":
        form = VolunteerExperienceForm(request.POST, instance=ve)
    else:
        form = VolunteerExperienceForm(instance=ve)

    if request.method == "POST" and form.is_valid():
        # ve = form.save(commit=False)
        # ve.user = request.user
        form.save()

        messages.success(request, "Process finished successfully")
        return redirect('edit_vexps')

    return render(request, template_name='edit/volunteer_experience.html', context={'form': form, 'title': title})

@user_login_required
def edit_volunteer_exps(request):
    vexps = VolunteerExperience.objects.filter(user=request.user)
    return render(request, 'edit/volunteer_experiences.html', {'vexps': vexps, 'title': 'Volunteer experiences'})

@user_login_required
def edit_language(request, pk=None):
    if pk:
        title = 'Edit language skill:'
        l = get_object_or_404(Language, pk=pk)
        if request.user != l.user:
            return HttpResponseForbidden()
    else:
        title = 'Add language skill:'
        l = Language()
        l.user = request.user

    # form = LanguageForm(request.POST or None, instance=l)
    if request.method == "POST":
        form = LanguageForm(request.POST, instance=l)
    else:
        form = LanguageForm(instance=l)

    if request.method == "POST" and form.is_valid():
        # l = form.save(commit=False)
        # l.user = request.user
        l.save()

        messages.success(request, "Language has been added successfully")
        return redirect('edit_student')

    return render(request, template_name='edit/language.html', context={'form': form, 'title': title})

@user_login_required
def edit_edu_exp(request, pk=None):
    if pk:
        title = 'Edit education experience:'
        edu = get_object_or_404(Education, pk=pk)
        if request.user != edu.user:
            return HttpResponseForbidden()
    else:
        title = 'Create education experience:'
        edu = Education()
        edu.user = request.user

    if request.method == "POST":
        form = EducationForm(request.POST, instance=edu)
    else:
        form = EducationForm(instance=edu)

    if request.method == "POST" and form.is_valid():
        # ve = form.save(commit=False)
        # ve.user = request.user
        form.save()

        messages.success(request, "Process finished successfully")
        return redirect('edit_edus')

    return render(request, template_name='edit/education.html', context={'form': form, 'title': title})

@user_login_required
def edit_edu_exps(request):
    edus = Education.objects.filter(user=request.user)
    return render(request, 'edit/educations.html', {'edus': edus, 'title': 'Education'})


@user_login_required
def delete_language(request, pk):
    l = get_object_or_404(Language, pk=pk)
    if request.user != l.user:
        return HttpResponseForbidden()
    l.delete()
    messages.success(request, "Languages block was changed!")
    return redirect('edit_student')

@user_login_required
def delete_we(request, pk):
    we = get_object_or_404(WorkingExperience, pk=pk)
    if request.user != we.user:
        return HttpResponseForbidden()
    we.delete()
    messages.success(request, "Working experience was deleted!")
    return redirect('edit_work_exps')

@user_login_required
def delete_ve(request, pk):
    ve = get_object_or_404(VolunteerExperience, pk=pk)
    if request.user != ve.user:
        return HttpResponseForbidden()
    ve.delete()
    messages.success(request, "Volunteer experience was deleted!")
    return redirect('edit_vexps')

@user_login_required
def delete_edu(request, pk):
    edu = get_object_or_404(Education, pk=pk)
    if request.user != edu.user:
        return HttpResponseForbidden()
    edu.delete()
    messages.success(request, "Education item was deleted!")
    return redirect('edit_edus')

from dal import autocomplete


class SoftSkillsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Skill.objects.none()

        qs = Skill.objects.filter(skill_type="soft")

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs.all()


class HardSkillsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Skill.objects.none()

        qs = Skill.objects.filter(skill_type="hard")

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs.all()


class ProgrammingLanguagesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Skill.objects.none()

        qs = Skill.objects.filter(skill_type="programming")

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs.all()


class SkillsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Skill.objects.none()

        qs = Skill.objects

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs.all()


@user_login_required
def search_form(request):
    return render(request, 'student/search.html')


def generate_cv(request, pk=None):
    u = get_object_or_404(get_user_model(), id=pk)
    context = dict(found_user=u, title="User", media="/media/")
    return render(request, "cv/index.html", context)


def show_preview(request, pk=None):
    u = get_object_or_404(get_user_model(), id=pk)
    context = dict(found_user=u, title="User", media="/media/")
    return render(request, "cv/cv_preview.html", context)


@user_login_required
def convertation(request, pk=None):
  #  pdf = "myCV.pdf"
    url = request.build_absolute_uri(reverse('show_cv', kwargs={'pk':pk}))
    pdf = settings.MEDIA_ROOT + '/student_cv/myCV.pdf'
    HTML(url).write_pdf(pdf, stylesheets=[CSS(string='@page { size: A4; margin: 0.0cm }')])
    '''   options = {
        'page-size': 'A4',
        'margin-top': '0.0in',
        'margin-right': '0.0in',
        'margin-bottom': '0.0in',
        'margin-left': '0.0in',
    }

    pdfkit.from_url(url, pdf, options=options)'''
    response = FileResponse(open(pdf, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + 'myCV.pdf'
    os.remove(pdf)
    return response


class LanguageAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Language.objects.none()

        qs = Language.objects

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs.all()

