from django.urls import path, include, re_path

from . import views

urlpatterns = [
    re_path(r'^create_internship/$', views.create_internship, name='create_internship')
]