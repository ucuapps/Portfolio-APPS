from django.urls import path, include, re_path

from . import views

urlpatterns = [
    re_path(r'^edit/student/$', views.edit_student, name='edit_student'),

    re_path(r'^edit/projects/$', views.edit_projects, name='edit_projects'),
    re_path(r'^edit/project/(?P<pk>\d+)/$', views.edit_project, name='edit_project'),
    re_path(r'^edit/new-project/$', views.edit_project, name='new_project'),

    re_path(r'^edit/working-experiences/$', views.edit_work_exps, name='edit_work_exps'),
    re_path(r'^edit/working-experience/(?P<pk>\d+)/$', views.edit_work_exp, name='edit_work_exp'),
    re_path(r'^edit/new-working-experience/$', views.edit_work_exp, name='new_work_exp'),
    re_path(r'^edit/delete-working-experience/(?P<pk>\d+)/$', views.delete_we, name='delete_we'),

    re_path(r'^edit/volunteer-experiences/$', views.edit_volunteer_exps, name='edit_vexps'),
    re_path(r'^edit/volunteer-experience/(?P<pk>\d+)/$', views.edit_volunteer_exp, name='edit_vexp'),
    re_path(r'^edit/new-volunteer-experience/$', views.edit_volunteer_exp, name='new_vexp'),
    re_path(r'^edit/delete-volunteer-experience/(?P<pk>\d+)/$', views.delete_ve, name='delete_vexp'),

    re_path(r'^edit/language/(?P<pk>\d+)/$', views.edit_language, name='edit_language'),
    re_path(r'^edit/new-language/$', views.edit_language, name='new_language'),
    re_path(r'^edit/delete-language/(?P<pk>\d+)/$', views.delete_language, name='delete_language'),

    # НЕ КОТЯН
    re_path(r'^soft-autocomplete/$', views.SoftSkillsAutocomplete.as_view(), name='soft-autocomplete'),
    re_path(r'^technical-autocomplete/$', views.TechnicalSkillsAutocomplete.as_view(), name='tech-autocomplete'),
    re_path(r'^professional-autocomplete/$', views.ProfessionalSkillsAutocomplete.as_view(), name='prof-autocomplete'),
]
