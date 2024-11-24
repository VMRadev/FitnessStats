from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from FitnessStats.accounts.models import Profile

UserModel = get_user_model()


class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("username","email",)
        # field_classes = {"username": UsernameField}


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']