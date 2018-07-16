from django.contrib import admin

from .models import Student, Project, WorkingExperience, VolunteerExperience, Skill, Language, StudyProgramme, \
    Certification, Hobby


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('user', 'study_programme', 'current_study_year', 'hard_skills', 'programming_language', 'soft_skills')


admin.site.register(StudyProgramme)
admin.site.register(Project)
admin.site.register(WorkingExperience)
admin.site.register(VolunteerExperience)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Certification)
admin.site.register(Hobby)
