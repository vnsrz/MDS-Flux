from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'number', 'email', 'cpf', 'address']
        labels = {
            'name' : 'Nome',
            'number' : 'Telefone',
            'address' : 'Endereço',
            'email': 'E-mail',
            'cpf' : 'CPF',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'number' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Apenas números',
                }),
            'email' : forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'exemplo@gmail.com',
            }),
            'cpf' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Apenas números',
            }),
            'address' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Ex: Qnm 14 bloco C - Taguatinga, DF',
            }),
        }

    def clean_cpf(self, *args, **kwargs):
        cpf = str(self.cleaned_data.get("cpf"))

        if not cpf.isnumeric():
            raise forms.ValidationError("CPF inválido, deve conter apenas números.")
        if len(cpf) != 11:
            raise forms.ValidationError("CPF inválido, deve conter 11 dígitos.")
        else:
            return cpf
    
    def clean_number(self, *args, **kwargs):
        number = str(self.cleaned_data.get("number"))

        if not number.isnumeric():
            raise forms.ValidationError("Número de telefone inválido, deve conter apenas números.")
        if len(number) != 11:
            raise forms.ValidationError("Número de telefone inválido, deve conter 11 dígitos.")
        else:
            return number