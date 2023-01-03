from django.db import models


class FirmModel(models.Model):
    name = models.CharField(max_length=50)
    mol = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    bulstat = models.CharField(max_length=9)
    idnum = models.CharField(max_length=11, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'firm'
