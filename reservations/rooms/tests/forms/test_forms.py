from django.test import TestCase

from rooms.forms import *


class FloorFormTest(TestCase):
    def test_form_save_successfuly(self):
        form = FloorForm(data={"name": 1})
        self.assertTrue(form.is_valid())
    
        
class BedFormTest(TestCase):
    def test_form_save_successfuly(self):
        form = BedsForm(data={
            "name": "Redovno",
            "name_short": "RL",
            "age": 99
        })
        self.assertTrue(form.is_valid())
        
    def test_not__save_when_not_needed_field_is_done(self):
        form = BedsForm(data={
            "name_short": "RL",
            "age": 99
        })
        self.assertFalse(form.is_valid())
