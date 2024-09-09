""" This script is the forms file of Members app"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms


class RegisterUserForm(UserCreationForm):
    """ This class registers users on the form"""
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=60,
    widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=60,
    widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        """Meta class"""
        model = User
        fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2')
    
    def __init__(self, *args, **kwargs):
        """Initializer of the forms"""
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'