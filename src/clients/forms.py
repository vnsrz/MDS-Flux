from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'number', 'email', 'cpf', 'address']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'number' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'exemplo@gmail.com',
            }),
            'cpf' : forms.TextInput(attrs={'class': 'form-control'}),
            'address' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Ex: Qnm 14 bloco C - Taguatinga, DF'
            }),
        }
