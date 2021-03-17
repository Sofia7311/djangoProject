from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    emailid = forms.EmailField(max_length=254, help_text='Required.',label = 'Email ID')
    #contact_number = forms.CharField(max_length = 10)

    class Meta:
        model = User
        fields = ('username', 'emailid', 'password1', 'password2', 'first_name', 'last_name')
