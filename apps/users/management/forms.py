from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm

from apps.users.models import User


class UserCreationForm(BaseUserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ("username",)
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
        }


class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ("username",)
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
        }
