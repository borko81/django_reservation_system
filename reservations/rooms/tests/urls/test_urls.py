from django.test import SimpleTestCase
from django.urls import resolve, reverse

from rooms.floor_views import *


class TestFloorUrls(SimpleTestCase):
    def test_floors_urls(self):
        url = reverse("rooms:floors")
        self.assertEqual(resolve(url).func, floors_show)

    def test_floor_create_url(self):
        url = reverse("rooms:floor_create")
        self.assertEqual(resolve(url).func, floor_create)

    def test_floor_edit_url(self):
        url = reverse("rooms:floor_edit", args=[1])
        self.assertEqual(resolve(url).func, floor_edit)

    def test_floor_delete_url(self):
        url = reverse("rooms:floor_delete", args=[1])
        self.assertEqual(resolve(url).func, floor_delete)
