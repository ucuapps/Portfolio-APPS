from django.db import models


from django.conf import settings


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    degree = models.CharField(max_length=255, blank=True, null=True)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    subjects = models.ManyToManyField(Subject, blank=True)
    about_me = models.TextField(blank=True, null=True, help_text="Enter here 1-5 sentences about you.")
