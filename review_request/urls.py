from django.urls import path, include, re_path

from . import views

urlpatterns = [
    re_path(r'^create-request/$', views.create_request, name='create_request'),
    re_path(r'^edit_request/(?P<pk>\d+)/$', views.create_request, name='edit_request'),

    re_path(r'^show_request/(?P<pk>\d+)/$', views.show_single_request, name='show_single_request'),
    re_path(r'^accept_request/(?P<pk>\d+)/$', views.accept_request, name='accept_request'),
    re_path(r'^user-show-requests/$', views.show_my_requests, name='show_my_requests'),
    re_path(r'^show-all-requests/$', views.show_all_requests, name='show_all_requests'),
]

