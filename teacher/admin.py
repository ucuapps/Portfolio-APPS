from django.contrib import admin

from .models import Teacher, Subject

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = ('user', 'degree', 'field_of_study', 'subjects', 'about_me')



admin.site.register(Subject)
