from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from rooms.models import FloorModel, BedModel, RoomTypeModel, RoomModel

from rooms.floor_views import *
from rooms.type_views import *
from rooms.bed_views import *
from rooms.rooms_views import *


class TestUrlsIsProtectedByUserLogin(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_need_user_login(self):
        response = self.client.get(reverse("rooms:floors"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("rooms:floor_create"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("rooms:floor_edit", args=[1]))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("rooms:floor_delete", args=[1]))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("rooms:bed"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("rooms:bed_create"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("rooms:bed_edit", args=[1]))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("rooms:bed_delete", args=[1]))
        self.assertEqual(response.status_code, 302)

        # Types

        response = self.client.get(reverse("rooms:type"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("rooms:types"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("rooms:type_create"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("rooms:type_edit", args=[1]))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("rooms:type_delete", args=[1]))
        self.assertEqual(response.status_code, 302)
        
        # Room
        rooms_urls = ["rooms:room", "rooms:rooms", "rooms:room_create"]
        room_edit_delete = ["rooms:room_edit", "rooms:room_delete"]
        
        for url_past in rooms_urls:
            response = self.client.get(reverse(url_past))
            self.assertEqual(response.status_code, 302)
            
        for url_past in room_edit_delete:
            response = self.client.get(reverse(url_past, args=[1]))
            self.assertEqual(response.status_code, 302)


class TestFloorTemplate(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")
        floor = FloorModel.objects.create(name=1)

    def test_floor_show_all(self):
        response = self.client.get(reverse("rooms:floors"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "floors/floors_show.html")

    def test_floor_create(self):
        response = self.client.get(reverse("rooms:floor_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "floors/floor_create.html")

    def test_floor_edit(self):
        response = self.client.get(reverse("rooms:floor_edit", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "floors/floor_create.html")

    def test_fllor_delete(self):
        response = self.client.get(reverse("rooms:floor_delete", args=[1]))
        self.assertEqual(response.status_code, 200)


class TestFloorTemplateError(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")

    def test_edit_and_delete_raise_error_when_not_found_anything(self):
        response = self.client.get(reverse("rooms:floor_edit", args=[1]))
        self.assertEqual(response.status_code, 404)

        response = self.client.get(reverse("rooms:floor_delete", args=[1]))
        self.assertEqual(response.status_code, 404)


class TestBedTemplateSuccess(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")
        BedModel.objects.create(name="Test")

    def test_show_all_beds(self):
        response = self.client.get(reverse("rooms:beds"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "beds/beds.html")

    def test_bed_create_template(self):
        response = self.client.get(reverse("rooms:bed_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "beds/bed_create.html")

    def test_bed_edit_template(self):
        response = self.client.get(reverse("rooms:bed_edit", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "beds/bed_create.html")

    def test_bed_delete(self):
        response = self.client.get(reverse("rooms:bed_delete", args=[1]))
        self.assertEqual(response.status_code, 200)


class TestRoomTypesTemplateSuccess(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")
        RoomTypeModel.objects.create(name="One", r_bed=1)

    def test_urls_for_room_types(self):
        response = self.client.get(reverse("rooms:type"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "types/base.html")

        response = self.client.get(reverse("rooms:types"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "types/types.html")

        response = self.client.get(reverse("rooms:type_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "types/create_type.html")

        response = self.client.get(reverse("rooms:type_edit", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "types/create_type.html")

        response = self.client.get(reverse("rooms:type_delete", args=[1]))
        self.assertEqual(response.status_code, 200)


class TestRoomTemplateUsageWhenUserSign(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")
        floor = FloorModel.objects.create(name=1)
        type = RoomTypeModel.objects.create(name="One", r_bed=1)
        RoomModel.objects.create(name="One", floor_id=floor, type_id=type)
        
    # Room
    def test_room_menu_template_usage(self):
        response = self.client.get(reverse("rooms:room"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/base.html')
        
    def test_room_show_template(self):
        response = self.client.get(reverse("rooms:rooms"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/rooms.html')
        
    def test_room_edit_template(self):
        response = self.client.get(reverse("rooms:room_edit", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/create_room.html')
        
    def test_room_create_template(self):
        response = self.client.get(reverse("rooms:room_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/create_room.html')
        
    def test_room_delete_template(self):
        response = self.client.get(reverse("rooms:room_delete", args=[1]))
        self.assertEqual(response.status_code, 200)