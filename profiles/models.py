from urllib.request import urlretrieve

from allauth.socialaccount.helpers import ImmediateHttpResponse
from django.core.files import File
from django.shortcuts import redirect
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from allauth.socialaccount.signals import pre_social_login
# from allauth.account.signals import user_signed_up, user_logged_in
from django.db.models.signals import post_save
from django.conf import settings
from allauth.account.utils import perform_login
from django.contrib.auth import get_user_model


from student.models import Student


class Interests(models.Model):
    INTEREST_TYPES = (
        ("professional", "Professional interest"),
        ("hobby", "Hobby")
    )

    interest_type = models.CharField(max_length=255, choices=INTEREST_TYPES)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    first_name = models.CharField(max_length=25, blank=True, null=True, help_text="Use English letters only")
    last_name = models.CharField(max_length=25, blank=True, null=True, help_text="Use English letters only")

    username = None
    email = models.EmailField(_('email address'), unique=True)

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    # TO DO format mobile number input
    mobile_number = models.CharField(max_length=25, blank=True, null=True, help_text="Enter your mobile number in the following format: +380*********")
    git_link = models.URLField(blank=True, null=True)
    fb_link = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(upload_to="profiles_img/%Y/%m/%d", blank=True, null=True)

    fields_of_interests = models.ManyToManyField(Interests, related_name="interests", blank=True)
    hobbies = models.ManyToManyField(Interests, related_name="hobbies", blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


@receiver(pre_social_login)
def link_to_local_user(sender, request, sociallogin, **kwargs):
    # email_address = sociallogin.account.extra_data['email']
    # users = User.objects.filter(email=email_address)
    #
    # if users:
    #     u = users[0]
    #     perform_login(request, u, email_verification=settings.ACCOUNT_EMAIL_VERIFICATION)
    #     raise ImmediateHttpResponse(redirect('home'))
    pass


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created and not (instance.is_student or instance.is_teacher):
        Student.objects.create(user=instance)
        instance.is_student = True
        instance.save()


from allauth.account.signals import user_signed_up, user_logged_in


@receiver(user_signed_up)
def social_login_fname_lname_profilepic(sociallogin, user, **kwargs):

    if sociallogin:

        if sociallogin.account.provider == 'google':
            f_name = sociallogin.account.extra_data['given_name']
            l_name = sociallogin.account.extra_data['family_name']
            if f_name:
                user.first_name = f_name
            if l_name:
                user.last_name = l_name

            picture_url = sociallogin.account.extra_data['picture']

            if picture_url:

                result = urlretrieve(picture_url)
                user.profile_image.save(
                    str(user.id)+".jpg",
                    File(open(result[0], "rb"))
                )
    user.save()
