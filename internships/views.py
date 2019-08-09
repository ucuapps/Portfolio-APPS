from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage

from profiles.models import User
from .models import Internship, Application
from .forms import CreateInternshipForm, ApplyToInternshipForm
from teacher.views import teacher_login_required
from student.views import student_login_required

from portfolio.settings import EMAIL_HOST_USER

from datetime import date


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
        send_mail('New internship at {}: {}'.format(internship.company_name, internship.position),
                  internship.description,
                  EMAIL_HOST_USER,
                  student_emails,
                  )

        messages.success(request, "Process finished successfully")
        return redirect('internships')

    return render(request, template_name='internship_edit.html', context={'form': form, 'title': title})


@student_login_required
def apply_to_internship(request, intern_id, pk=None):
    title = 'Apply to internship:'
    application = Application()
    internship = Internship.objects.get(id=intern_id)
    application.internship = internship
    application.applicant = request.user.student

    internship.applicants.add(request.user.student)

    if request.method == "POST":
        form = ApplyToInternshipForm(request.POST, request.FILES, instance=application)
    else:
        form = ApplyToInternshipForm(instance=application)

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(request, "Process finished successfully")
        return redirect('internships')

    return render(request, template_name='internship_apply.html', context={'form': form, 'title': title,
                                                                           'intern_id': intern_id})


@student_login_required
def edit_application(request, intern_id):
    title = 'Edit application:'
    curr_internship = Internship.objects.get(id=intern_id)
    my_app = Application.objects.get(internship=curr_internship)
    application = get_object_or_404(Application, pk=my_app.id)

    if application.sent:
        messages.error(request, "You can't edit application that has been already sent")
        return redirect('internships')

    if curr_internship.deadline < date.today():
        messages.error(request, "This internship is already overdue")
        return redirect('internships')

    if request.method == "POST":
        form = ApplyToInternshipForm(request.POST, request.FILES, instance=application)
    else:
        form = ApplyToInternshipForm(instance=application)

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(request, "Process finished successfully")
        return redirect('internships')

    return render(request, template_name='internship_apply.html', context={'form': form, 'title': title,
                                                                           'intern_id': intern_id})


@student_login_required
def apply_outer_intern(request, pk):
    internship = get_object_or_404(Internship, pk=pk)

    if internship.deadline < date.today():
        messages.error(request, "This internship is already overdue")
        return redirect('internships')

    internship.applicants.add(request.user.student)
    application, created = Application.objects.get_or_create(internship=internship,
                                                             applicant=request.user.student)
    application.save()

    return redirect(internship.link)


@student_login_required
def send_application(request, intern_id):
    internship = Internship.objects.get(id=intern_id)
    try:
        application = Application.objects.get(internship=internship)
        application.sent = True
        application.save()

        header = 'New application to {} internship'.format(internship.company_name)
        student_name = request.user.first_name + ' ' + request.user.last_name
        letter_body = '''
        {} application to {} position in {}
        Motivation letter:
        {}
        
        Find CV attached
        '''.format(student_name, internship.position, internship.company_name,
                   application.motivation_letter)
        teacher_email = [internship.created_by.email]

        email = EmailMessage(
            header,  # letter header
            letter_body,  # letter body
            EMAIL_HOST_USER,  # from
            teacher_email,  # to
        )
        email.attach_file(application.cv.path)
        email.send()

        return redirect('internships')
    except Application.DoesNotExist:
        messages.warning(request, "Please save your application before sending it")
        return redirect('apply_to_internship', intern_id)

