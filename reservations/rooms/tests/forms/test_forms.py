from django.test import TestCase

from rooms.forms import *


class FloorFormTest(TestCase):
    def test_form_save_successfuly(self):
        form = FloorForm(data={"name": 1})
        self.assertTrue(form.is_valid())
