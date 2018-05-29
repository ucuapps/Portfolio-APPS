from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import ContactForm


@login_required
def contact(request):
    title = 'Contact'
    template = 'contact.html'
    form = ContactForm(request.POST or None)

    if form.is_valid():
        print("Sending email")
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['name']

        emailFrom = form.cleaned_data['email']
        # emailFrom = settings.EMAIL_HOST_USER
        emailTo = [settings.EMAIL_HOST_USER]
        subject = "[Portfolio.APPS] Contact form"
        message = "From:%s\nName:%s\nMessage:%s" % (emailFrom, name, comment)
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Success!"
        messages.success(request, "Your message was sent, thank you :*")
        form = None
    context = dict(
        title=title, form=form
    )
    return render(request, template, context)
