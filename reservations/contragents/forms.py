from django.forms import ModelForm

from .models import FirmModel


from rooms.forms import BaseForms


class ContragentForm(BaseForms, ModelForm):
    class Meta:
        model = FirmModel
        fields = "name mol address bulstat idnum is_active".split()
        
        labels = {
            "name": "Име",
            "mol": "МОЛ",
            "address": "Адрес",
            "bulstat": "Булстат",
            "idnum": "Булстат по ДДС",
            "is_active": "Активен"
        }