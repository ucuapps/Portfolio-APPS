from django.urls import path, include, re_path

from . import views
urlpatterns = [
    re_path(r'^$', views.index, name='home'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^edit/user/$', views.edit_user, name='edit_user'),
    re_path(r'^users-autocomplete/$', views.UsersAutocomplete.as_view(), name='users-autocomplete'),
    re_path(r'^user/(?P<pk>\d+)/$', views.show_user, name='show-user'),
    re_path(r'^search/$', views.search, name='search_user'),
    re_path(r'^interests-autocomplete/$', views.InterestsAutocomplete.as_view(), name='interests-autocomplete'),
    re_path(r'^hobby-autocomplete/$', views.HobbyAutocomplete.as_view(), name='hobby-autocomplete'),
    re_path(r'^internships/$', views.show_internships, name='internships')
]
