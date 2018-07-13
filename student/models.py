from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Language(models.Model):
    LANGUAGES = (
        ('Afrikaans', 'Afrikaans'),
         ('Arabic', 'Arabic'),
         ('Asturian', 'Asturian'),
         ('Azerbaijani', 'Azerbaijani'),
         ('Bulgarian', 'Bulgarian'),
         ('Belarusian', 'Belarusian'),
         ('Bengali', 'Bengali'),
         ('Breton', 'Breton'),
         ('Bosnian', 'Bosnian'),
         ('Catalan', 'Catalan'),
         ('Czech', 'Czech'),
         ('Welsh', 'Welsh'),
         ('Danish', 'Danish'),
         ('German', 'German'),
         ('Lower Sorbian', 'Lower Sorbian'),
         ('Greek', 'Greek'),
         ('English', 'English'),
         ('Australian English', 'Australian English'),
         ('British English', 'British English'),
         ('Esperanto', 'Esperanto'),
         ('Spanish', 'Spanish'),
         ('Argentinian Spanish', 'Argentinian Spanish'),
         ('Colombian Spanish', 'Colombian Spanish'),
         ('Mexican Spanish', 'Mexican Spanish'),
         ('Nicaraguan Spanish', 'Nicaraguan Spanish'),
         ('Venezuelan Spanish', 'Venezuelan Spanish'),
         ('Estonian', 'Estonian'),
         ('Basque', 'Basque'),
         ('Persian', 'Persian'),
         ('Finnish', 'Finnish'),
         ('French', 'French'),
         ('Frisian', 'Frisian'),
         ('Irish', 'Irish'),
         ('Scottish Gaelic', 'Scottish Gaelic'),
         ('Galician', 'Galician'),
         ('Hebrew', 'Hebrew'),
         ('Hindi', 'Hindi'),
         ('Croatian', 'Croatian'),
         ('Upper Sorbian', 'Upper Sorbian'),
         ('Hungarian', 'Hungarian'),
         ('Interlingua', 'Interlingua'),
         ('Indonesian', 'Indonesian'),
         ('Ido', 'Ido'),
         ('Icelandic', 'Icelandic'),
         ('Italian', 'Italian'),
         ('Japanese', 'Japanese'),
         ('Georgian', 'Georgian'),
         ('Kabyle', 'Kabyle'),
         ('Kazakh', 'Kazakh'),
         ('Khmer', 'Khmer'),
         ('Kannada', 'Kannada'),
         ('Korean', 'Korean'),
         ('Luxembourgish', 'Luxembourgish'),
         ('Lithuanian', 'Lithuanian'),
         ('Latvian', 'Latvian'),
         ('Macedonian', 'Macedonian'),
         ('Malayalam', 'Malayalam'),
         ('Mongolian', 'Mongolian'),
         ('Marathi', 'Marathi'),
         ('Burmese', 'Burmese'),
         ('Norwegian Bokmål', 'Norwegian Bokmål'),
         ('Nepali', 'Nepali'),
         ('Dutch', 'Dutch'),
         ('Norwegian Nynorsk', 'Norwegian Nynorsk'),
         ('Ossetic', 'Ossetic'),
         ('Punjabi', 'Punjabi'),
         ('Polish', 'Polish'),
         ('Portuguese', 'Portuguese'),
         ('Brazilian Portuguese', 'Brazilian Portuguese'),
         ('Romanian', 'Romanian'),
         ('Russian', 'Russian'),
         ('Slovak', 'Slovak'),
         ('Slovenian', 'Slovenian'),
         ('Albanian', 'Albanian'),
         ('Serbian', 'Serbian'),
         ('Serbian Latin', 'Serbian Latin'),
         ('Swedish', 'Swedish'),
         ('Swahili', 'Swahili'),
         ('Tamil', 'Tamil'),
         ('Telugu', 'Telugu'),
         ('Thai', 'Thai'),
         ('Turkish', 'Turkish'),
         ('Tatar', 'Tatar'),
         ('Udmurt', 'Udmurt'),
         ('Ukrainian', 'Ukrainian'),
         ('Urdu', 'Urdu'),
         ('Vietnamese', 'Vietnamese'),
         ('Simplified Chinese', 'Simplified Chinese'),
         ('Traditional Chinese', 'Traditional Chinese'),
    )
    # ToDo: lang LVLs
    LEVEL = (
        ("A1", "Beginner"),
        ("A2", "Elementary"),
        ("B1", "Intermediate"),
        ("B2", "Upper Intermediate"),
        ("C1", "Advanced"),
        ("C2", "Proficient"),
    )

    name = models.CharField(max_length=255, choices=LANGUAGES)
    level = models.CharField(max_length=255, choices=LEVEL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
    project_field = models.CharField(max_length=20, default="", help_text="Word/words/abbreviation which describes your project."
                                                      " Example: ML, WEB, IOT, NLP, CV, AI, Design, Networks, BA,"
                                                      " Visualization, Robotics, Data Mining, Software, Security, "
                                                      "Analysis, Economics", blank=False)
    title = models.CharField(max_length=60, help_text="Project title. Example: Health Care project", blank=False)
    about = models.TextField()
    technologies = models.ManyToManyField(Skill, blank=True)

    # TODO: mentor
    collaborators = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)


class VolunteerExperience(models.Model):
    title = models.CharField(max_length=60, help_text="Event title. Example: ML Conference", blank=False)
    description = models.TextField(max_length=150)
    link = models.URLField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    organization = models.CharField(max_length=225, blank=True, null=True)


class Education(models.Model):
    degree = models.CharField(max_length=30)
    period_start = models.DateField(null=True, blank=True)
    period_end = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=130)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    university = models.CharField(max_length=225, blank=True, null=True)
    field_of_study = models.CharField(max_length=225, blank=True, null=True)


class WorkingExperience(models.Model):
    occupation = models.CharField(max_length=255,default="", help_text="Example: Back-end dev")
    company = models.CharField(max_length=255, null=True, blank=True)
    period_start = models.DateField(null=True, blank=True)
    period_end = models.DateField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    description = models.TextField(blank=True, null=True, help_text="Fill the field with description"
                                                                    " of your responsibilities, gained experience")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class StudyProgramme(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Hobby(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Certification(models.Model):
    title = models.CharField(max_length=60, help_text="Please fill the field with the certificate name "
                                                      "Example: Data Science Summer School")
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
    hobbies = models.ManyToManyField(Skill, blank=True)

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
