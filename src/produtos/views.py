from django.shortcuts import render
from .models import Produto


# Create your views here.
def list_products (request):
    produtos= Produto.objects.all()
    return render (request, 'produtos.html', {'produtos' : produtos})
