from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^create_internship/$', views.create_internship, name='create_internship'),
    re_path(r'^apply_to_internship/(?P<intern_id>\d+)/$', views.apply_to_internship, name='apply_to_internship'),
    re_path(r'apply_outer_intern/(?P<pk>\d+)/$', views.apply_outer_intern, name='apply_outer_intern'),
    re_path(r'^edit_application/(?P<intern_id>\d+)/$', views.edit_application, name='edit_application'),
    re_path(r'^send_application/(?P<intern_id>\d+)/$', views.send_application, name='send_application')
]
