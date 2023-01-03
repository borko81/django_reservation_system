from django.test import SimpleTestCase
from django.urls import reverse, resolve

from contragents.views import *


"""
urlpatterns = [
    path("", views.menu, name="menu"),
    path("contragents/", views.contragents, name="contragents"),
    path("create/", views.create, name="create"),
    path("edit/<int:id>/", views.edit, name="edit"),
]
"""

class TestContragentUrls(SimpleTestCase):
    def test_contragent_menu_url(self):
        url = reverse("contragent:menu")
        self.assertEqual(resolve(url).func, menu)
        
    def test_show_all_url(self):
        url = reverse("contragent:contragents")
        self.assertEqual(resolve(url).func, contragents)
        
    def test_create_new_url(self):
        url = reverse("contragent:create")
        self.assertEqual(resolve(url).func, create)
        
    def test_edit_url(self):
        url = reverse("contragent:edit", args=[1])
        self.assertEqual(resolve(url).func, edit)
    