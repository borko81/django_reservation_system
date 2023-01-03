from django.test import TestCase

from contragents.models import FirmModel
from contragents.forms import ContragentForm


class TestContragentForm(TestCase):
    def test_form_is_valid(self):
        form = ContragentForm(
            data={
                "name": "Test",
                "mol": "Test Test",
                "address": "Velingrad",
                "bulstat": 111111111,
                "idnum": "BG111111111",
                "is_active": True,
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_raise_error_when_not_full(self):
        form = ContragentForm(data={})
        self.assertFalse(form.is_valid())
        errors = form.errors
        self.assertIn("name", errors)
        self.assertIn("mol", errors)
        self.assertIn("address", errors)
        self.assertIn("bulstat", errors)
