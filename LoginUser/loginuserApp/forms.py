from django import forms
from django.core import validators


class LoginForm(forms.Form):
    userName = forms.CharField(required=False, validators=
    [validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    password = forms.CharField(widget=forms.PasswordInput)
