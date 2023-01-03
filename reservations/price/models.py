from django.db import models

from rooms.models import BedModel, RoomTypeModel


class Contract(models.Model):

    FOODS = [
        ("NO", "NIGHT_ONLY"),
        ("BB", "BB"),
        ("HB", "HB"),
        ("FB", "FB"),
    ]

    name = models.CharField(max_length=120, unique=True)
    food = models.CharField(max_length=2, choices=FOODS, default="NO")
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Periods(models.Model):
    name = models.CharField(max_length=32)
    from_data = models.DateField()
    to_data = models.DateField()

    def __str__(self):
        return self.name


class BedsShuffle(models.Model):
    beds_names = models.CharField(max_length=100)
    type = models.ForeignKey(RoomTypeModel, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.full_name = "".join(self.beds_name, self.type.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Price(models.Model):
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    period_id = models.ForeignKey(Periods, on_delete=models.CASCADE)
    bed = models.ForeignKey(BedsShuffle, on_delete=models.CASCADE)
    price = models.FloatField()
    is_valid = models.BooleanField(default=True)
