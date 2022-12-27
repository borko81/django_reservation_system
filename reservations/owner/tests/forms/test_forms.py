from django.test import TestCase

from owner.forms import *
from owner.models import OwnerModel


class TestOwnerForm(TestCase):
    def test_ownerdata_form(self):
        form = OwnerDataForm(
            data={
                "name": "Фирма име",
                "mol": "Мол",
                "address": "Адрес",
                "bulstat": "1234",
                "idnum": "bg123",
                "tel": "тел",
            }
        )
        self.assertTrue(form.is_valid())

    def test_owner_data_form_with_incorect_bulstat_type_should_raise_error(self):
        form = OwnerDataForm(
            data={
                "name": "Фирма име",
                "mol": "Мол",
                "address": "Адрес",
                "bulstat": "nevalden",
                "idnum": "bg123",
                "tel": "тел",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["bulstat"][0], "Enter a whole number.")


class TestOwnerBankForm(TestCase):
    def test_form_is_save_successfully_when_all_is_corect(self):
        owner = OwnerModel.objects.create(
            name="Borko",
            mol="Boris Stoilov",
            address="Velingrad",
            tel="08784455",
            http="https://google.bg",
            email="korea60@abv.bg",
            bulstat="445588774",
            idnum="BG445588774",
        )
        form = OwnerBankForm(
            data={
                "name": "Име",
                "kod": "BIC",
                "smetka": "12345",
                "owner_id": owner,
            }
        )
        self.assertTrue(form.is_valid())
        
    def test_form_raise_error_when_required_is_missing(self):
        form = OwnerBankForm(
            data = {
                
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['name'][0], 'This field is required.')
        self.assertEquals(form.errors['kod'][0], 'This field is required.')
        self.assertEquals(form.errors['smetka'][0], 'This field is required.')
        self.assertEquals(form.errors['owner_id'][0], 'This field is required.')
        
        
class TestOWnerLastFakId(TestCase):
    def test_form_save_when_all_is_right(self):
        form = OwnerLastFakIdForm(
            data={
                'last_fak_id': 1,
                'last_pr_id': 1
            }
        )
        self.assertTrue(form.is_valid())
