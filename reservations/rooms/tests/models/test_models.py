from django.db import IntegrityError
from django.test import TestCase
from django.core.validators import ValidationError

from rooms.models import BedModel, FloorModel, RoomTypeModel, RoomModel


class FloorModelTest(TestCase):
    def setUp(self):
        floor_test = FloorModel(name=1)
        floor_test.save()

    def test_successfully_create_floor(self):
        f = FloorModel.objects.all().first()
        self.assertEqual(f.name, 1)

    def test_raise_error_if_found_duplicate_name(self):
        with self.assertRaises(IntegrityError) as er:
            new_floor = FloorModel.objects.create(name=1)

        self.assertEqual(
            str(er.exception), "UNIQUE constraint failed: rooms_floormodel.name"
        )


class BedModelTest(TestCase):
    def setUp(self):
        bed = BedModel(name="Редовно легло", name_short="РЛ")
        bed.save()
        
    def test_bed_create_successfully(self):
        self.assertEqual(len(BedModel.objects.all()), 1)
        
    def test_try_duplicate_name_raise_error(self):
        with self.assertRaises(IntegrityError) as er:
            BedModel.objects.create(name="Редовно легло", name_short="РЛ")