from django import forms

from . import models


class BaseForms:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class FloorForm(BaseForms, forms.ModelForm):
    class Meta:
        model = models.FloorModel
        fields = "name".split()

        labels = {"name": "Етаж"}
        
        
class BedsForm(BaseForms, forms.ModelForm):
    class Meta:
        model = models.BedModel
        fields = 'name name_short age dop'.split()
        
        labels = {"name": "Име", "name_short": "Кратко име", "dop": "Допълнително", "age": "Макс. възр."}


class RoomTypeForm(BaseForms, forms.ModelForm):
    class Meta:
        model = models.RoomTypeModel
        fields = 'name name_short r_bed d_bed allow_one_only'.split()
        
        labels = {
            "name": "Име",
            "name_short": "Кратко име",
            "r_bed": "Редовни легла макс",
            "d_bed": "Допълнителни легла макс",
            "allow_one_only": "Сам в стая"
        }
        
        
class RoomForm(BaseForms, forms.ModelForm):
    class Meta:
        model = models.RoomModel
        fields = "name description floor_id type_id".split()
        
        labels = {
            "name": "Име",
            "type_id": "Тип стая",
            "description": "Описание",
            "floor_id": "Етаж"
        }