from django.test import SimpleTestCase
from django.urls import resolve, reverse

from rooms.floor_views import *
from rooms.bed_views import *


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


class TestBedsUlrs(SimpleTestCase):
    def test_bed_menu_url(self):
        url = reverse("rooms:bed")
        self.assertEqual(resolve(url).func, beds_menu)

    def test_beds_show_url(self):
        url = reverse("rooms:beds")
        self.assertEqual(resolve(url).func, beds_show)

    def test_bed_create_url(self):
        url = reverse("rooms:bed_create")
        self.assertEqual(resolve(url).func, bed_create)

    def test_bed_edit_url(self):
        url = reverse("rooms:bed_edit", args=[1])
        self.assertEqual(resolve(url).func, bed_edit)

    def test_bed_delete(self):
        url = reverse("rooms:bed_delete", args=[1])
        self.assertEqual(resolve(url).func, bed_delete)
