from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Language(models.Model):
    LANGUAGES = (
        ('af', 'Afrikaans'),
         ('ar', 'Arabic'),
         ('ast', 'Asturian'),
         ('az', 'Azerbaijani'),
         ('bg', 'Bulgarian'),
         ('be', 'Belarusian'),
         ('bn', 'Bengali'),
         ('br', 'Breton'),
         ('bs', 'Bosnian'),
         ('ca', 'Catalan'),
         ('cs', 'Czech'),
         ('cy', 'Welsh'),
         ('da', 'Danish'),
         ('de', 'German'),
         ('dsb', 'Lower Sorbian'),
         ('el', 'Greek'),
         ('en', 'English'),
         ('en-au', 'Australian English'),
         ('en-gb', 'British English'),
         ('eo', 'Esperanto'),
         ('es', 'Spanish'),
         ('es-ar', 'Argentinian Spanish'),
         ('es-co', 'Colombian Spanish'),
         ('es-mx', 'Mexican Spanish'),
         ('es-ni', 'Nicaraguan Spanish'),
         ('es-ve', 'Venezuelan Spanish'),
         ('et', 'Estonian'),
         ('eu', 'Basque'),
         ('fa', 'Persian'),
         ('fi', 'Finnish'),
         ('fr', 'French'),
         ('fy', 'Frisian'),
         ('ga', 'Irish'),
         ('gd', 'Scottish Gaelic'),
         ('gl', 'Galician'),
         ('he', 'Hebrew'),
         ('hi', 'Hindi'),
         ('hr', 'Croatian'),
         ('hsb', 'Upper Sorbian'),
         ('hu', 'Hungarian'),
         ('ia', 'Interlingua'),
         ('id', 'Indonesian'),
         ('io', 'Ido'),
         ('is', 'Icelandic'),
         ('it', 'Italian'),
         ('ja', 'Japanese'),
         ('ka', 'Georgian'),
         ('kab', 'Kabyle'),
         ('kk', 'Kazakh'),
         ('km', 'Khmer'),
         ('kn', 'Kannada'),
         ('ko', 'Korean'),
         ('lb', 'Luxembourgish'),
         ('lt', 'Lithuanian'),
         ('lv', 'Latvian'),
         ('mk', 'Macedonian'),
         ('ml', 'Malayalam'),
         ('mn', 'Mongolian'),
         ('mr', 'Marathi'),
         ('my', 'Burmese'),
         ('nb', 'Norwegian Bokmål'),
         ('ne', 'Nepali'),
         ('nl', 'Dutch'),
         ('nn', 'Norwegian Nynorsk'),
         ('os', 'Ossetic'),
         ('pa', 'Punjabi'),
         ('pl', 'Polish'),
         ('pt', 'Portuguese'),
         ('pt-br', 'Brazilian Portuguese'),
         ('ro', 'Romanian'),
         ('ru', 'Russian'),
         ('sk', 'Slovak'),
         ('sl', 'Slovenian'),
         ('sq', 'Albanian'),
         ('sr', 'Serbian'),
         ('sr-latn', 'Serbian Latin'),
         ('sv', 'Swedish'),
         ('sw', 'Swahili'),
         ('ta', 'Tamil'),
         ('te', 'Telugu'),
         ('th', 'Thai'),
         ('tr', 'Turkish'),
         ('tt', 'Tatar'),
         ('udm', 'Udmurt'),
         ('uk', 'Ukrainian'),
         ('ur', 'Urdu'),
         ('vi', 'Vietnamese'),
         ('zh-hans', 'Simplified Chinese'),
         ('zh-hant', 'Traditional Chinese'),
    )
    # ToDo: lang LVLs
    LEVEL = (
        ("bad", "Beginner"),
        ("good", "Intermediate"),
        ("excellent", "Advanced")
    )

    name = models.CharField(max_length=255, choices=LANGUAGES)
    level = models.CharField(max_length=255, choices=LEVEL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Skill(models.Model):
    SKILL_TYPES = (
        ("hard", "Hard skill"),
        ("soft", "Soft skill"),
        ("programming", "Programming languages")
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
    description = models.TextField(max_length=700)
    link = models.URLField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    organization = models.CharField(max_length=225, blank=True, null=True)


class Education(models.Model):
    degree = models.CharField(max_length=255)
    period_start = models.DateField(null=True, blank=True)
    period_end = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=700)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    university = models.CharField(max_length=225, blank=True, null=True)
    field_of_study = models.CharField(max_length=225, blank=True, null=True)


class WorkingExperience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    period_start = models.DateField(null=True, blank=True)
    period_end = models.DateField(null=True, blank=True)
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
    hard_skills = models.ManyToManyField(Skill, related_name="hard_skills", blank=True)
    programming_languages = models.ManyToManyField(Skill, related_name="programming_languages", blank=True)
    soft_skills = models.ManyToManyField(Skill, related_name="soft_skills", blank=True)

    summary = models.TextField(blank=True, null=True, help_text="Enter here 1-5 sentences about you. EX: Honors student"
                                                                " with record of academic and extracurricular success. "
                                                                "Extensive leadership experience, particularly within a"
                                                                " higher education setting."
                                                                "Adept at working across departments, with faculty,"
                                                                " administrators")

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
