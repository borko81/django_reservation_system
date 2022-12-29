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
