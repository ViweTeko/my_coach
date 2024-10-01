""" This script is the forms file of Members app"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.forms import ModelForm, HiddenInput
from .models import Member


class RegisterUserForm(UserCreationForm):
    """ This class registers users on the form"""
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
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
        'password2'
        )
    
    def __init__(self, *args, **kwargs):
        """Initializer of the forms"""
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class AthleteForm(ModelForm):
    """This class is the athlete form"""
    class Meta:
        """Meta class"""
        model = Member
        fields = '__all__'
        labels = {
            'id': '',
            'name': '',
            'surname': '',
            'gender': '',
            'age': '',
            'club': '',
            'athlete_event': '',
            'athlete_image': '',
        }
        widgets = {
            'id': HiddenInput,
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
            'gender': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Gender'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'club': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Club'}),
            'athlete_event': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event'}),
            'athlete_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
        }