from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=60, required=False, help_text="First name")
    last_name = forms.CharField(max_length=60, required=False, help_text="Last name")
    email = forms.EmailField(
        max_length=254, help_text="Add a valid email address", required=False,
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

