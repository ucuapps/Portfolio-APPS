from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from .models import Internship
from .forms import CreateInternshipForm
from teacher.views import teacher_login_required
from student.views import student_login_required


@teacher_login_required
# @student_login_required
def create_internship(request, pk=None):
    if pk:
        title = 'Edit internship:'
        internship = get_object_or_404(Internship, pk=pk)
    else:
        title = 'Create internship:'
        internship = Internship()
        internship.created_by = request.user

    if request.method == "POST":
        form = CreateInternshipForm(request.POST, instance=internship)
    else:
        form = CreateInternshipForm(instance=internship)

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(request, "Process finished successfully")
        return redirect('internships')

    return render(request, template_name='internship_edit.html', context={'form': form, 'title': title})


@student_login_required
def apply_to_internship(request, pk=None):
    return render(request, template_name='internship_apply.html')
