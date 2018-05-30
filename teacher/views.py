from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


from .models import Teacher
from .forms import TeacherForm

teacher_login_required = user_passes_test(lambda u: u.is_teacher, login_url='/')


def user_login_required(view_func):
    decorated_view_funct = login_required(teacher_login_required(view_func))
    return decorated_view_funct


@user_login_required
def edit_teacher(request):
    template = "edit/teacher.html"
    context = {}

    # form = TeacherForm(request.POST or None, instance=request.user.teacher)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=request.user.teacher)
    else:
        form = TeacherForm(instance=request.user.teacher)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your profile data has been changed")
    context["form"] = form
    return render(request, template, context)
