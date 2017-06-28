from django.conf.urls import patterns, url
# from
# from django.views.generic import TemplateView
from . import views
# from views import ProjectCreate, ProjectUpdate, ProjectDelete

urlpatterns = [
    # url(r'', views.projects, name="projects"),
    url(r'^$', views.list_projects, name="project_list"),
    url(r'^ongoing$', views.list_ongoing_projects, name="project_list_on"),
    url(r'^complete$', views.list_complete_projects, name="project_list_cp"),
    url(r'^new/$', views.new_project, name="new_project"),
    url(r'(?P<pk>\d+)/$', views.project_detail, name="project_detail"),
    url(r'(?P<pk>\d+)/edit/$', views.project_edit, name="edit_project"),
    # url(r'^edit$', views.edit_project, name="edit_project"),
    # url(r'new/$', ProjectCreate.as_view(), name='new_project'),
    # url(r'(?P<pk>[0-9]+)/$', ProjectUpdate.as_view(), name='project_update'),
    # url(r'(?P<pk>[0-9]+)/delete/$', ProjectDelete.as_view(), name='project_delete'),
]
