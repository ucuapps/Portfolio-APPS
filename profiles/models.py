from allauth.socialaccount.helpers import ImmediateHttpResponse
from django.shortcuts import redirect
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from allauth.socialaccount.signals import pre_social_login
from django.db.models.signals import post_save
from django.conf import settings
from allauth.account.utils import perform_login


from student.models import Student


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

    username = None
    email = models.EmailField(_('email address'), unique=True)

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    mobile_number = models.CharField(max_length=25, blank=True, null=True)
    git_link = models.URLField(blank=True, null=True)
    fb_link = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(upload_to="profiles_img/%Y/%m/%d", blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


@receiver(pre_social_login)
def link_to_local_user(sender, request, sociallogin, **kwargs):
    email_address = sociallogin.account.extra_data['email']
    users = User.objects.filter(email=email_address)
    if users:
        perform_login(request, users[0], email_verification=settings.ACCOUNT_EMAIL_VERIFICATION)
        raise ImmediateHttpResponse(redirect('home'))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not (instance.is_student or instance.is_teacher):
        Student.objects.create(user=instance)
