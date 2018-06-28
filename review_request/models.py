from django.db import models
from django.conf import settings


from student.models import Skill


class ReviewRequest(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    deadline = models.DateField()
    skills = models.ManyToManyField(Skill, blank=True)

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_requestor")
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="teacher_reviewer")
    accepted = models.BooleanField(default=False)

