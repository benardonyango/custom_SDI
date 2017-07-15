# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from datetime import datetime

from . import views
from .models import Project

# Create your tests here.


class ProjectModelTest(TestCase):

    def create_default_project(self):
        my_project = Project.objects.create(
            title='My test project',
            description='Blank n blind test description',
            sname='BBTD',
            organization='JDEV',
            start_date='2000-01-01',
            end_date='2017-07-14',
            image='/home/jdev/Pictures/IAMROOT.jpg',  # use dynamic asset
            status='ON',
        )

    def to_date(self, date):
        return datetime.strptime(date, '%Y-%m-%d').date()

    def test_saving_and_retrieving_projects(self):
        self.create_default_project()
        self.assertEqual(Project.objects.count(), 1)

        project = Project.objects.first()
        self.assertEqual(project.status, 'ON')
        self.assertEqual(project.title, 'My test project')

    def test_updating_projects(self):
        self.create_default_project()
        self.assertEqual(Project.objects.count(), 1)

        # retrieve, edit and update project
        p = Project.objects.first()
        p.title = 'Edited Project Title'
        p.description = 'Edited description'
        p.sname = 'ED'
        p.organization = 'ECORP'
        p.start_date = self.to_date('2000-12-11')
        p.end_date = self.to_date('2017-07-15')
        p.image = '/home/jdev/Downloads/farechart.jpg'
        p.status = 'CP'
        p.save()

        project = Project.objects.first()
        self.assertEqual(project.title, 'Edited Project Title')
        self.assertNotEqual(project.title, 'My test project')

        self.assertEqual(project.description, 'Edited description')
        self.assertNotEqual(project.description,
                            'Blank n blind test description')

        self.assertEqual(project.sname, 'ED')
        self.assertNotEqual(project.sname, 'BBTD')

        self.assertEqual(project.organization, 'ECORP')
        self.assertNotEqual(project.organization, 'JDEV')

        self.assertEqual(project.start_date, self.to_date('2000-12-11',))
        self.assertNotEqual(project.start_date, self.to_date('2000-01-01',))

        self.assertEqual(project.end_date, self.to_date('2017-07-15',))
        self.assertNotEqual(project.end_date, self.to_date('2017-07-14',))

        self.assertEqual(project.image, '/home/jdev/Downloads/farechart.jpg')
        self.assertNotEqual(project.image,
                            '/home/jdev/Pictures/IAMROOT.jpg')

        self.assertEqual(project.status, 'CP')
        self.assertNotEqual(project.status, 'ON')

    def test_can_delete_project(self):
        self.create_default_project()

        self.assertEqual(Project.objects.count(), 1)

        project = Project.objects.first()
        project.delete()

        self.assertEqual(Project.objects.count(), 0)


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
