from django.urls import path, include, re_path

from . import views

urlpatterns = [
    re_path(r'^edit/teacher/$', views.edit_teacher, name='edit_teacher'),
    re_path(r'^subjects-autocomplete/$', views.SubjectsAutocomplete.as_view(), name='subjects-autocomplete'),

]
