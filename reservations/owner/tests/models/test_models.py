from django.core.exceptions import ValidationError
from django.test import TestCase

from owner.models import OwnerModel, OwnerBank, OwnerLastFakIdModel


class TestOwner(TestCase):
    
    def setUp(self):
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
    
    def test_model_successfully_created(self):
        o = OwnerModel.objects.get(id=1)
        self.assertEqual(o.name, "Borko")
        
    def test_change_name_with_big_value(self):
        o = OwnerModel.objects.get(id=1)
        
        with self.assertRaises(ValidationError):
            o.name = 'A' * 55
            o.full_clean()
            
        with self.assertRaises(ValidationError) as e:
            o.mol = 'A' * 121
            o.full_clean()

        
        
class TestOwnerBank(TestCase):
    def setUp(self):
        o = OwnerModel.objects.create(
            name="Borko",
            mol="Boris Stoilov",
            address="Velingrad",
            tel="08784455",
            http="https://google.bg",
            email="korea60@abv.bg",
            bulstat="445588774",
            idnum="BG445588774",
        )
        OwnerBank.objects.create(
            name="Bank",
            kod="AB123",
            smetka="12345678",
            owner_id=o
        )
        
    def test_check_correct_save_in_models(self):
        self.assertEqual(len(OwnerBank.objects.all()), 1)
        self.assertEqual(
            OwnerBank.objects.get(id=1).owner_id.name, "Borko"
        )
        
    def test_when_try_to_put_more_char_in_kod_raise_error(self):
        o = OwnerBank.objects.get(id=1)
        with self.assertRaises(ValidationError) as er:
            o.kod = 'A' * 9
            o.full_clean()
            


class TestOwnerFakId(TestCase):
    def setUp(self):
        fak = OwnerLastFakIdModel(
            last_fak_id=1,
            last_pr_id=1
        )
        fak.save()
        
    def test_correct_fill_with_zeros(self):
        f = OwnerLastFakIdModel.objects.get(id=1)
        self.assertEqual(f.last_fak_id, '0000000001')