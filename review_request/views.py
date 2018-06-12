from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from .models import ReviewRequest
from .forms import ReviewRequestForm
from student.views import student_login_required
from teacher.views import teacher_login_required


def notify_teachers(request):
    send_mail(
        '[Portfolio.APPS] Review:',
        'Hello from Portfolio, %s is asking for review' % request.student.email,
        'from@example.com',
        list(get_user_model().objects.filter(is_teacher=True).values_list('email', flat=True).all()),
        fail_silently=False,
    )


@teacher_login_required
def show_all_requests(request):
    title = "Pending unaccepted requests"
    requests = ReviewRequest.objects.filter(accepted=False).all()
    return render(request, 'review_request/show_all.html', {'requests': requests, 'title': title})


@teacher_login_required
def show_single_request(request, pk):
    req = get_object_or_404(ReviewRequest, id=pk)
    return render(request, 'review_request/show_single.html', dict(req=req,
                                                                   title="Review request"))


@teacher_login_required
def accept_request(request, pk):
    req = get_object_or_404(ReviewRequest, id=pk)
    if not req.accepted:
        messages.success(request, "Accepted")
        req.accepted = True
        req.save()
        req.teacher = request.user
        req.save()
    else:
        messages.error(request, "Request was already accepted!")
    return redirect('show_my_requests')


@login_required
def show_my_requests(request):
    title = "Pending requests"
    if request.user.is_teacher:
        requests = ReviewRequest.objects.filter(teacher=request.user).all()
    else:
        requests = ReviewRequest.objects.filter(student=request.user).all()
    return render(request, 'review_request/custom_show.html', {'requests': requests, 'title': title})


@student_login_required
def create_request(request, pk=None):
    new_form = False
    if pk:
        title = 'Edit request:'
        review_request = get_object_or_404(ReviewRequest, pk=pk)
        if request.user != review_request.student:
            return HttpResponseForbidden()
    else:
        title = 'Create request:'
        review_request = ReviewRequest()
        review_request.student = request.user
        new_form = True

    if request.method == "POST":
        form = ReviewRequestForm(request.POST, instance=review_request)
    else:
        form = ReviewRequestForm(instance=review_request)

    if request.method == "POST" and form.is_valid():
        # r = form.save()
        # r.student = request.user
        # r.save()
        # rev_request = form.save(commit=False)
        # rev_request.student = request.user
        a = form.save()
        # rev_request.m2m_save()

        if new_form:
            # notify_teachers(review_request)
            pass
        messages.success(request, "Process finished successfully")
        return redirect('show_my_requests')

    return render(request, template_name='review_request/edit.html', context={'form': form, 'title': title})
