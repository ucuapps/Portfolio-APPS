from django.db import models
from django.conf import settings

from student.models import Student


class Internship(models.Model):
    company_name = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    description = models.TextField()
    link = models.URLField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deadline = models.DateField()
    is_inner = models.BooleanField(default=True)

    applicants = models.ManyToManyField(Student, related_name="applicants", blank=True)
    approved_applicants = models.ManyToManyField(Student, related_name="approved_applicants", blank=True)

    def __str__(self):
        return self.company_name


class Application(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Student, on_delete=models.CASCADE)

    cv = models.FileField()
    motivation_letter = models.TextField(blank=True, null=True)

    sent = models.BooleanField(default=False)
