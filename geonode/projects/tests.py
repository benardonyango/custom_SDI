# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from . import views
from .models import Project

# Create your tests here.


class AllProjectsPageTest(TestCase):

    def test_project_list_url_resolves_to_list_projects_view(self):
        found = resolve('/projects/')
        self.assertEqual(found.func, views.list_projects)

    def test_project_list_page_uses_correct_template(self):
        response = self.client.get('/projects/')
        self.assertTemplateUsed(response, 'projects/projects.html')

    def test_reply_when_no_projects_created(self):
        self.assertEqual(Project.objects.count(), 0)

        response = self.client.get('/projects/')
        self.assertContains(
            response,
            'There are no projects created yet.')

    def test_list_all_projects(self):
        ongoing_project = Project.objects.create(
            title='Test ongoing project', status='ON',
            image='/home/jdev/Pictures/IAMROOT.jpg')
        completed_project = Project.objects.create(
            title='Test completed project', status='CP',
            image='/home/jdev/Pictures/IAMROOT.jpg')

        response = self.client.get('/projects/')

        self.assertContains(response, ongoing_project.title)
        self.assertContains(response, completed_project.title)


class OngoingProjectsPageTest(TestCase):

    def test_project_list_on_url_resolves_to_list_projects_view(self):
        found = resolve('/projects/ongoing/')
        self.assertEqual(found.func, views.list_ongoing_projects)

    def test_project_list_on_page_uses_correct_template(self):
        response = self.client.get('/projects/ongoing/')
        self.assertTemplateUsed(response, 'projects/projects.html')

    def test_reply_when_no_ongoing_project(self):
        self.assertEqual(Project.objects.count(), 0)

        response = self.client.get('/projects/ongoing/')
        self.assertContains(
            response,
            'There are no continuing projects currently.')

    def test_list_only_ongoing_projects(self):
        ongoing_project = Project.objects.create(
            title='Test ongoing project', status='ON',
            image='/home/jdev/Pictures/IAMROOT.jpg')
        completed_project = Project.objects.create(
            title='Test completed project', status='CP',
            image='/home/jdev/Pictures/IAMROOT.jpg')

        response = self.client.get('/projects/ongoing/')

        self.assertContains(response, ongoing_project.title)
        self.assertNotContains(response, completed_project.title)


class CompletedProjectsPageTest(TestCase):

    def test_project_list_cp_url_resolves_to_list_projects_view(self):
        found = resolve('/projects/completed/')
        self.assertEqual(found.func, views.list_completed_projects)

    def test_project_list_cp_page_uses_correct_template(self):
        response = self.client.get('/projects/completed/')
        self.assertTemplateUsed(response, 'projects/projects.html')

    def test_reply_when_no_completed_project(self):
        self.assertEqual(Project.objects.count(), 0)

        response = self.client.get('/projects/completed/')
        self.assertContains(
            response,
            'There are no completed projects yet.')

    def test_list_only_completed_projects(self):
        ongoing_project = Project.objects.create(
            title='Test ongoing project', status='ON',
            image='/home/jdev/Pictures/IAMROOT.jpg')
        completed_project = Project.objects.create(
            title='Test completed project', status='CP',
            image='/home/jdev/Pictures/IAMROOT.jpg')

        response = self.client.get('/projects/completed/')

        self.assertContains(response, completed_project.title)
        self.assertNotContains(response, ongoing_project.title)


# class ProjectModelTest(TestCase):

#     def test_can_create_and_save_project(self):
#         pass

#     def test_can_update_project(self):
#         pass

#     def test_can_delete_project(self):
#         pass
