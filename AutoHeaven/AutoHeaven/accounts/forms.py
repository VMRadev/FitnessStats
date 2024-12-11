from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, SetPasswordMixin
from django import forms
from django.utils.translation import gettext_lazy as _

from AutoHeaven.accounts.models import Profile

UserModel = get_user_model()


class AccountCreationForm(UserCreationForm):
    password1, password2 = SetPasswordMixin.create_password_fields()

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("username", "email",)
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email address"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes and placeholders to the password fields
        self.fields['password1'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Enter password",
        })
        self.fields['password2'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Confirm password",
        })


class CustomLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter model name', "autofocus": True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter model name', "autocomplete": "current-password"}),
    )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'age': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'preferred_transmission': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Preferred Transmission'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Profile Image'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description of you'}),
        }
