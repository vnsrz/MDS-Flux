from django import forms
from .models import Purchase, Sale
from apps.clients.models import Client

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['products', 'provider', 'price']
        labels = {
            'products' : 'Produtos',
            'provider' : 'Fornecedor',
            'price' : 'Valor total',
        }
        products = forms.CharField()
        widgets = {
            'products' : forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder' : 'Ex: Camiseta Masculina x5 R$200',
            }),
            'provider' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : '',
            }),
            'price' : forms.NumberInput(attrs={
                'class': 'form-control',
            }),
        }


class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(SaleForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.filter(user=user)
    
    class Meta:
        model = Sale
        fields = ['products', 'client', 'price']
        labels = {
            'products' : 'Produtos',
            'client' : 'Cliente',
            'price' : 'Valor total',
        }

        widgets = {
            'products' : forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder' : 'Ex: Camiseta Masculina x5 R$200',
            }),
            'client' : forms.Select(
                attrs={'class': 'form-control'}),
                
            'price' : forms.NumberInput(attrs={
                'class': 'form-control',
            }),
        }
        