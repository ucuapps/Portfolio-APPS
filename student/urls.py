from django.urls import path, include, re_path

from . import views

urlpatterns = [
    #re_path(r'^student/(?P<pk>\d+)$', views.show_student, name='show_student'),

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

    re_path(r'^edit/educations/$', views.edit_edu_exps, name='edit_edus'),
    re_path(r'^edit/education/(?P<pk>\d+)/$', views.edit_edu_exp, name='edit_edu'),
    re_path(r'^edit/new-education/$', views.edit_edu_exp, name='new_edu'),
    re_path(r'^edit/delete-education/(?P<pk>\d+)/$', views.delete_edu, name='delete_edu'),


    re_path(r'^edit/language/(?P<pk>\d+)/$', views.edit_language, name='edit_language'),
    re_path(r'^edit/new-language/$', views.edit_language, name='new_language'),
    re_path(r'^edit/delete-language/(?P<pk>\d+)/$', views.delete_language, name='delete_language'),


    re_path(r'^soft-autocomplete/$', views.SoftSkillsAutocomplete.as_view(), name='soft-autocomplete'),
    re_path(r'^hard-autocomplete/$', views.HardSkillsAutocomplete.as_view(), name='hard-autocomplete'),
    re_path(r'^planguage-autocomplete/$', views.ProgrammingLanguagesAutocomplete.as_view(),\
            name='planguage-autocomplete'),
    re_path(r'^skills-autocomplete/$', views.SkillsAutocomplete.as_view(), name='skills-autocomplete'),
    re_path(r'^language-autocomplete/$', views.LanguageAutocomplete.as_view(), name='language-autocomplete'),
    re_path(r'^projects-autocomplete/$', views.CvProjectsAutocomplete.as_view(), name='projects-autocomplete'),
    re_path(r'^volunteering-autocomplete/$', views.CvVolunteerExpsAutocomplete.as_view(), name='volunteer-autocomplete'),
    re_path(r'^working-autocomplete/$', views.CvWorkingExpAutocomplete.as_view(), name='working-autocomplete'),

    re_path(r'^cv-soft-autocomplete/$', views.CvSoftSkillsAutocomplete.as_view(), name='cv-soft-autocomplete'),
    re_path(r'^cv-hard-autocomplete/$', views.CvHardSkillsAutocomplete.as_view(), name='cv-hard-autocomplete'),
    re_path(r'^cv-plang-autocomplete/$', views.CvProgrammingLanguagesAutocomplete.as_view(),\
            name='cv-plang-autocomplete'),

    re_path(r'^generate-cv/(?P<pk>\d+)/$', views.edit_cv, name="edit_cv"),
    re_path(r'^show-cv/(?P<pk>\d+)/$', views.generate_cv, name='show_cv'),
    re_path(r'^generate-pdf/(?P<pk>\d+)/$', views.generate_cv, name='generate_pdf'),
]
