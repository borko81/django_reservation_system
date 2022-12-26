from django import forms

from . import models


class BootstrapWidget:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class OwnerDataForm(BootstrapWidget, forms.ModelForm):
    class Meta:
        model = models.OwnerModel
        fields = "__all__"
        labels = {
            "name": "Фирма име",
            "mol": "Мол",
            "address": "Адрес",
            "bulstat": "Булстат",
            "idnum": "Ид номер",
            "tel": "тел",
        }


class OwnerBankForm(BootstrapWidget, forms.ModelForm):
    class Meta:
        model = models.OwnerBank
        fields = "__all__"
        labels = {
            "name": "Име",
            "kod": "BIC",
            "smetka": "IBAN",
            "owner_id": "Собственик",
        }


class OwnerLastFakIdForm(BootstrapWidget, forms.ModelForm):
    class Meta:
        model = models.OwnerLastFakIdModel
        fields = "__all__"
        labels = {
            "last_fak_id": "Последен номер за фактура",
            "last_pr_id": "Последен номер за проформа",
        }
