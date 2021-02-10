from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from project_user.models import Profile


class RegisterStaffForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'email',
        ]


class EditStaffProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]


class EditStaffPasswordForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]



class RegisterClientForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'email',
        ]


class EditClientProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]


class EditClientPasswordForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]



class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'address',
        ]
