from django.db import models
from django.conf import settings

class Internship(models.Model):
    name = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    description = models.TextField()
    link = models.URLField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # TODO: Add applicants field

    def __str__(self):
        return self.name