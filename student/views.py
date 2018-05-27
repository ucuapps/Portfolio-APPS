from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib import messages

from .forms import StudentForm, ProjectForm, WorkingExperienceForm, VolunteerExperienceForm, LanguageForm
from .models import Project, WorkingExperience, VolunteerExperience, Language, Skill


def edit_student(request):
    template = "edit/student.html"
    context = {}

    form = StudentForm(request.POST or None, instance=request.user.student)
    if request.POST and form.is_valid():
        form.save()
        messages.success(request, "Your profile data has been changed")
    context["form"] = form
    context["languages"] = Language.objects.filter(user=request.user)
    return render(request, template, context)


def edit_project(request, pk=None):
    if pk:
        title = 'Edit project:'
        project = get_object_or_404(Project, pk=pk)
        if request.user not in project.collaborators.all():
            return HttpResponseForbidden()
    else:
        title = 'Create project:'
        project = Project()

    form = ProjectForm(request.POST or None, instance=project)
    if request.POST and form.is_valid():
        project = form.save()
        project.collaborators.add(request.user)
        project.save()

        messages.success(request, "Process finished successfully")
        return redirect('edit_projects')

    return render(request, template_name='edit/project.html', context={'form': form, 'title': title})


def edit_projects(request):
    projects = Project.objects.filter(collaborators=request.user).distinct()
    return render(request, 'edit/projects.html', context={'projects': projects, 'title': "Projects"})


def edit_work_exp(request, pk=None):
    if pk:
        title = 'Edit working experience:'
        we = get_object_or_404(WorkingExperience, pk=pk)
        if request.user != we.user:
            return HttpResponseForbidden()
    else:
        title = 'Create working experience:'
        we = WorkingExperience()

    form = WorkingExperienceForm(request.POST or None, instance=we)
    if request.POST and form.is_valid():
        we = form.save(commit=False)
        we.user = request.user
        we.save()

        messages.success(request, "Process finished successfully")
        return redirect('edit_work_exps')

    return render(request, template_name='edit/work_experience.html', context={'form': form, 'title': title})


def edit_work_exps(request):
    work_exps = WorkingExperience.objects.filter(user=request.user)
    return render(request, 'edit/work_experiences.html', {'work_exps': work_exps, 'title': 'Working experiences'})


def edit_volunteer_exp(request, pk=None):
    if pk:
        title = 'Edit volunteer experience:'
        ve = get_object_or_404(VolunteerExperience, pk=pk)
        if request.user != ve.user:
            return HttpResponseForbidden()
    else:
        title = 'Create volunteer experience:'
        ve = VolunteerExperience()

    form = VolunteerExperienceForm(request.POST or None, instance=ve)
    if request.POST and form.is_valid():
        ve = form.save(commit=False)
        ve.user = request.user
        ve.save()

        messages.success(request, "Process finished successfully")
        return redirect('edit_vexps')

    return render(request, template_name='edit/volunteer_experience.html', context={'form': form, 'title': title})


def edit_volunteer_exps(request):
    vexps = VolunteerExperience.objects.filter(user=request.user)
    return render(request, 'edit/volunteer_experiences.html', {'vexps': vexps, 'title': 'Volunteer experiences'})


def edit_language(request, pk=None):
    if pk:
        title = 'Edit language skill:'
        l = get_object_or_404(Language, pk=pk)
        if request.user != l.user:
            return HttpResponseForbidden()
    else:
        title = 'Add language skill:'
        l = Language()

    form = LanguageForm(request.POST or None, instance=l)
    if request.POST and form.is_valid():
        l = form.save(commit=False)
        l.user = request.user
        l.save()

        messages.success(request, "Language has been added successfully")
        return redirect('edit_student')

    return render(request, template_name='edit/language.html', context={'form': form, 'title': title})


def delete_language(request, pk):
    l = get_object_or_404(Language, pk=pk)
    if request.user != l.user:
        return HttpResponseForbidden()
    l.delete()
    messages.success(request, "Languages block was changed!")
    return redirect('edit_student')


def delete_we(request, pk):
    we = get_object_or_404(WorkingExperience, pk=pk)
    if request.user != we.user:
        return HttpResponseForbidden()
    we.delete()
    messages.success(request, "Working experience was deleted!")
    return redirect('edit_work_exps')


def delete_ve(request, pk):
    ve = get_object_or_404(VolunteerExperience, pk=pk)
    if request.user != ve.user:
        return HttpResponseForbidden()
    ve.delete()
    messages.success(request, "Volunteer experience was deleted!")
    return redirect('edit_vexps')


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


class ProfessionalSkillsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Skill.objects.none()

        qs = Skill.objects.filter(skill_type="professional")

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs.all()


class TechnicalSkillsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Skill.objects.none()

        qs = Skill.objects.filter(skill_type="technical")

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs.all()
