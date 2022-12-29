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
