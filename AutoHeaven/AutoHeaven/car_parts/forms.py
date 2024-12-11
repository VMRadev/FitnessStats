from django import forms
from AutoHeaven.car_parts.models import CarPart



class CarPartBaseForm(forms.ModelForm):
    class Meta:
        model = CarPart
        exclude = ('owner', 'category',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car price'}),
            'description': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Enter car type'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter car colour'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Enter car image'}),
        }


class CarPartCreateForm(CarPartBaseForm):
    pass

class CarPartUpdateForm(CarPartBaseForm):
    pass

class CarPartDeleteForm(CarPartBaseForm):
    pass


