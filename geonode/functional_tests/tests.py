from django.test import LiveServerTestCase
from django.test import Client
from selenium import webdriver
import time


class StandardUserProjectsTest(LiveServerTestCase):
    # Our favorite user, Jake, is looking for a source of spatial data
    # on agricultural, livestock and soils data in Kenya
    # Hes heard of the numerous datasets in KALRO KSS but he's ish ish
    # about going to the office in person, hes a busy lad aight.

    # So since he knows of the new geoportal hosted by KALRO, he goes
    # online, exploratory hat on the head, clicky mouse in hand

    def setUp(self):
        self.browser = webdriver.Chrome()
        # self.browser.implicitly_wait(2)

    def login(self):
        # Logs in to the site
        self.client.login(username='jdev', password='jdeveloper')

    def test_user_can_load_our_portal_and_view_all_projects(self):
        # He visits the portal and decides to checkout the projects page
        self.browser.get(self.live_server_url + '/projects/')
        # He notices a title, Explore Projects
        title = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Explore Projects', title)
        # He notices there are no projects created yet
        message = self.browser.find_element_by_class_name('lead').text
        self.assertIn('There are no projects created yet.', message)

        # Next, he clicks to see ongoing projects
        self.browser.get(self.live_server_url + '/projects/ongoing/')
        message = self.browser.find_element_by_class_name('lead').text
        self.assertIn('There are no continuing projects currently.', message)

        # To confirm, he clicks to see completed projects
        self.browser.get(self.live_server_url + '/projects/completed/')
        message = self.browser.find_element_by_class_name('lead').text
        self.assertIn('There are no completed projects yet.', message)

        # Oh wow, if only he had administrative access!
        # So he calls the admin who logs in ...
        # And creates a project

        # Then with the admin loged out, Jake now checks to see what
        # ze portal has to offer
        # Alas! from the project summary, he can see the number of
        # layers, documents and maps, wow

        # What if he expanded the project to see more?
        # Alas! from the project, he can view maps
        # And layers
        # And even documents!

    def tearDown(self):
        self.browser.close()


# class AdminUserProjectsTest(LiveServerTestCase):

#     def setUp(self):
#         # Kalmin, you know, the admin, goes on a test adventure
#         self.browser = webdriver.Chrome()
#         self.client.login(username='jdev', password='jdeveloper')
#         session = self.client.session

#         session['id'] = 'mytestsession'
#         session.save()

#         cookie = self.client.cookies[session['id']]
#         self.browser.get(self.live_server_url + '/admin/')
#         self.browser.refresh()
#         self.browser.add_cookie(
#             {
#                 'name': session['id'],
#                 'value': cookie.value,
#                 'secure': False,
#                 'path': '/',
#             })

#     def test_projects_page(self):
#         self.browser.get(self.live_server_url + '/projects/')
#         time.sleep(10)

#     def tearDown(self):
#         self.browser.close()
