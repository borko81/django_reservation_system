from django.db import models


class ContractAndOwner(models.Model):
    name = models.CharField(max_length=50)
    mol = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    bulstat = models.IntegerField()
    idnum = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True


class OwnerModel(ContractAndOwner):
    http = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    tel = models.CharField(max_length=13, blank=True, null=True)
    logo = models.ImageField(upload_to="owner_image", blank=True, null=True)


class OwnerBank(models.Model):
    name = models.CharField(max_length=100)
    kod = models.CharField(max_length=8)
    smetka = models.CharField(max_length=30)
    owner_id = models.ForeignKey(OwnerModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class OwnerLastFakIdModel(models.Model):
    last_fak_id = models.CharField(
        max_length=10, null=True, blank=True, default="0000000001"
    )
    last_pr_id = models.CharField(
        max_length=10, null=True, blank=True, default="0000000001"
    )

    def __str__(self) -> str:
        return f"Last fak is {self.last_fak_id} last pr is {self.last_pr_id}"

    def save(self, *args, **kwargs):
        self.last_fak_id = str(int(self.last_fak_id)).zfill(10)
        self.last_pr_id = str(int(self.last_pr_id)).zfill(10)
        super().save(*args, **kwargs)
