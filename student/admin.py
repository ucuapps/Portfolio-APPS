from django.contrib import admin


from .models import Student, Project, WorkingExperience, VolunteerExperience, Skill


admin.site.register(Student)
admin.site.register(Project)
admin.site.register(WorkingExperience)
admin.site.register(VolunteerExperience)
admin.site.register(Skill)
