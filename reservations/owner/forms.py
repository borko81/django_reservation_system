from django import forms

from . import models


class OwnerDataForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
    
    class Meta:
        model = models.OwnerModel
        fields = '__all__'
        labels = {
            "name": "Фирма име",
            "mol": "Мол",
            "address": "Адрес",
            "bulstat": "Булстат",
            "idnum": "Ид номер",
            "tel": "тел"
        }

        