from django.db import models
from django.conf import settings


class Language(models.Model):
    LANGUAGES = (
        ("uk", "Ukrainian"),
    )
    # ToDo: lang LVLs
    LEVEL = (
        ("bad", "Bad LVL"),
        ("good", "Good LVL"),
        ("excellent", "Excellent LVL")
    )

    name = models.CharField(max_length=255, choices=LANGUAGES)
    level = models.CharField(max_length=255, choices=LEVEL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Skill(models.Model):
    SKILL_TYPES = (
        ("professional", "Professional skill"),
        ("soft", "Soft skill"),
        ("technical", "Technical skill")
    )

    skill_type = models.CharField(max_length=255, choices=SKILL_TYPES)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    technologies = models.ManyToManyField(Skill, blank=True)
    # TODO: mentor
    collaborators = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)


class VolunteerExperience(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    organization = models.CharField(max_length=225, blank=True, null=True)


class WorkingExperience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    period_start = models.DateTimeField(null=True, blank=True)
    period_end = models.DateTimeField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class StudyProgramme(models.Model):
    name = models.CharField(max_length=255)


class Certification(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="%Y/%m/%d")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Student(models.Model):
    STUDY_YEARS = (
        (1, "First year"),
        (2, "Second year"),
        (3, "Third year"),
        (4, "Fourth year")
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # study programme
    study_programme = models.ForeignKey(StudyProgramme, on_delete=models.CASCADE, blank=True, null=True)
    current_study_year = models.IntegerField(choices=STUDY_YEARS, blank=True, null=True)

    # Skills
    professional_skills = models.ManyToManyField(Skill, related_name="professional_skills", blank=True)
    technical_skills = models.ManyToManyField(Skill, related_name="technical_skills", blank=True)
    soft_skills = models.ManyToManyField(Skill, related_name="soft_skills", blank=True)

    # Projects
    # projects = models.ManyToManyField(Project, blank=True)

    # Languages
    # languages

    # Working exp
    # working_experience = None

    # Volunteer exp
    # volunteer_experience = None

    # Certifications
    # certifications = None
