from django.db import models


class BedModel(models.Model):
    name = models.CharField(max_length=120, unique=True)
    name_short = models.CharField(max_length=5)
    dop = models.BooleanField(default=False)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class FloorModel(models.Model):
    name = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return str(self.name)


class RoomTypeModel(models.Model):
    name = models.CharField(max_length=15, unique=True)
    name_short = models.CharField(max_length=5, unique=True, null=True, blank=True)
    r_bed = models.IntegerField(default=1)
    d_bed = models.IntegerField(blank=True, null=True)
    allow_one_only = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.name_short:
            self.name_short = self.name[:5]
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class RoomModel(models.Model):
    name = models.CharField(max_length=12, unique=True)
    description = models.CharField(max_length=120, null=True, blank=True)
    floor_id = models.ForeignKey(FloorModel, on_delete=models.SET_NULL, null=True, blank=True)
    type_id = models.ForeignKey(RoomTypeModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
