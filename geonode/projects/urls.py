from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^$', views.list_projects, name="project_list"),
    url(r'^ongoing/$', views.list_ongoing_projects, name="project_list_on"),
    url(r'^completed/$', views.list_completed_projects, name="project_list_cp"),
    url(r'^new$', views.new_project, name="new_project"),
    url(r'(?P<pk>\d+)/$', views.project_detail, name="project_detail"),
    url(r'(?P<pk>\d+)/edit/$', views.project_edit, name="edit_project"),
]
