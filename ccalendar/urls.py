from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('json/', views.loadnext, name='loadnext'),
    path('list/',views.list, name='list'),
    path('resources/', views.resources, name='resources'),
    path('buildings/', views.buildings, name='buildings')
]