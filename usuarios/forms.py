from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Ej: correo@ejemplo.com", "autocomplete": "off"}
        )
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(
                attrs={"placeholder": "Ej: usuario123", "autocomplete": "off"}
            )
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Ej: usuario123", "autocomplete": "off"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "password", "autocomplete": "off"}
        )
    )
