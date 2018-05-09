from django.urls import path, include, re_path

from .views import index

urlpatterns = [
    re_path(r'^$', index),
]
