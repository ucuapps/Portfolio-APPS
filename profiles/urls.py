from django.urls import path, include, re_path

from . import views
urlpatterns = [
    re_path(r'^$', views.index, name='home'),
    re_path(r'^about/$', views.about, name='about'),
]
