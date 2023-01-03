from django.test import TestCase


from contragents.models import FirmModel

"""
    name = models.CharField(max_length=50)
    mol = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    bulstat = models.IntegerField()
    idnum = models.CharField(max_length=13, blank=True, null=True)
    is_active = models.BooleanField(default=True)
"""


class TestFirmModel(TestCase):
    def setUp(self):
        firm = FirmModel(name="Test", mol="Test Test Test", address="Velingrad", bulstat=11223344)
        firm.save()
        
    def test_firm_is_ok(self):
        self.assertEqual(FirmModel.objects.all().first().name, "Test")
        