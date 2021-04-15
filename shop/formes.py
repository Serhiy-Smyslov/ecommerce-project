from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SingUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    second_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=100,
                             help_text='serhiy.smyslov@gmail.com')

    class Meta:
        model = User
        fields = ('first_name', 'second_name',
                  'username', 'password1', 'password2',)