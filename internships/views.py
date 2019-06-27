from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail

from .models import Internship, Application
from .forms import CreateInternshipForm, ApplyToInternshipForm
from teacher.views import teacher_login_required
from student.views import student_login_required


@teacher_login_required
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
        students = User.objects.filter(is_student=True)
        student_emails = list([student.email for student in students])
        teacher_email = internship.created_by.email
        send_mail('New internship at {}: {}'.format(internship.name, internship.position),
                  internship.description,
                  teacher_email,
                  student_emails,
                  )

        messages.success(request, "Process finished successfully")
        return redirect('internships')

    return render(request, template_name='internship_edit.html', context={'form': form, 'title': title})


@student_login_required
def apply_to_internship(request, pk=None):
    if pk:
        title = 'Edit application:'
        application = get_object_or_404(Application, pk=pk)

        if application.sent:
            messages.error(request, "You can't edit application that has been already sent")
            return redirect('internships')

    else:
        title = 'Apply to internship:'
        application = Application()
        application.internship = internship

    if request.method == "POST":
        form = ApplyToInternshipForm(request.POST, instance=application)
    else:
        form = ApplyToInternshipForm(instance=application)

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(request, "Process finished successfully")
        return redirect('internships')

    return render(request, template_name='internship_apply.html', context={'form': form, 'title':title})
