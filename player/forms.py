from django import forms
from django.forms import ModelForm
from .models import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        
        fields = ('player_name', 'player_email', 'player_contact', 'player_profession', 'player_salary',)

        widgets = {
            'player_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'player_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'player_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact No.'}),
            'player_profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profession'}),
            'player_salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
        }