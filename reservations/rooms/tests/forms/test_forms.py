from django.test import TestCase

from rooms.forms import *


class FloorFormTest(TestCase):
    def test_form_save_successfuly(self):
        form = FloorForm(data={"name": 1})
        self.assertTrue(form.is_valid())


class BedFormTest(TestCase):
    def test_form_save_successfuly(self):
        form = BedsForm(data={"name": "Redovno", "name_short": "RL", "age": 99})
        self.assertTrue(form.is_valid())

    def test_not__save_when_not_needed_field_is_done(self):
        form = BedsForm(data={"name_short": "RL", "age": 99})
        self.assertFalse(form.is_valid())


class RoomTypeFormTest(TestCase):
    def test_form_save_success(self):
        form = RoomTypeForm(
            data={
                "name": "Име",
                "name_short": "123",
                "r_bed": 1,
                "d_bed": 0,
                "allow_one_only": True
            }
        )
        self.assertTrue(form.is_valid())
        
    def test_form_not_save_when_filed_is_too_big(self):
        form = RoomTypeForm(
            data={
                "name": "Име",
                "name_short": "123456",
                "r_bed": 1,
                "d_bed": 0,
                "allow_one_only": True
            }
        )
        self.assertFalse(form.is_valid())
