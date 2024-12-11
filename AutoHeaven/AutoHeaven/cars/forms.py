from django import forms

from AutoHeaven.cars.choices import CarTypeChoices
from AutoHeaven.cars.models import Car, CarModel, CarBrand, CarSpecs


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner', 'brand', 'model')

        widgets = {
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car price'}),
            'type': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Enter car type'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car colour'}),
            'status': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Enter car status'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter car year'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Enter car image'}),
        }


class CarCreateForm(CarBaseForm):
    pass
    # class Meta(CarBaseForm.Meta):
    #     widgets = {
    #         'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car price'}),
    #         'type': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Enter car type'}),
    #         'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car colour'}),
    #         'status': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Enter car status'}),
    #         'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter car year'}),
    #         'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Enter car image'}),
    #     }


class CarUpdateForm(CarBaseForm):
    pass

class CarDeleteForm(CarBaseForm):
    pass


class CarModelBaseForm(forms.ModelForm):
    class Meta:
        model = CarModel
        exclude = ('brand',)
        widgets = {
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter model name'})
        }


class CarModelCreateForm(CarModelBaseForm):
    pass
    # class Meta(CarModelBaseForm.Meta):
    #     widgets = {
    #         'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter model name'})
    #     }

class CarModelUpdateForm(CarModelBaseForm):
    pass


class CarBrandBaseForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields= '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter brand name'})
        }


class CarBrandCreateForm(CarBrandBaseForm):
    pass
    # class Meta(CarBrandBaseForm.Meta):
    #     widgets = {
    #         'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter brand name'})
    #     }

class CarBrandUpdateForm(CarBrandBaseForm):
    pass


class CarSpecsBaseForm(forms.ModelForm):
    class Meta:
        model = CarSpecs
        exclude = ('car', 'id')

        widgets = {
            'engine': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Engine of the car'}),
            'mileage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mileage of the car'}),
            'fuel_consumption': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fuel consumption of the car per 100km'}),
            'max_speed': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max Speed of the car'}),
            'fuel_type': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Fuel Type'}),
            'max_distance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max Distance of one full tank of fuel'}),
            'transmission': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Transmission of the car'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description of the car'}),
        }


class CarSpecsEditForm(CarSpecsBaseForm):
    pass

