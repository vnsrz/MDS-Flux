from django.shortcuts import render
from django.shortcuts import redirect, render
from apps import user

from apps.transactions.models import Purchase, Sale
from .forms import PurchaseForm, SaleForm

# Lista compras
def list_purchases (request):
    id = request.user.id
    purchases= Purchase.objects.filter(user=id)
    
    return render (request, 'transactions/purchases.html', {'purchases' : purchases})

# Lista vendas
def list_sales (request):
    id = request.user.id
    sales= Sale.objects.filter(user=id)
    
    return render (request, 'transactions/sales.html', {'sales' : sales})

# Cria compras
def create_purchase (request):
    form = PurchaseForm(request.POST or None)

    if form.is_valid():
        purchase = form.save(commit=False)
        purchase.user = request.user
        purchase.save()
        return redirect(list_purchases)

    return render(request, 'transactions/purchase-form.html', {'form': form})

# Cria vendas
def create_sale (request):
    form = SaleForm(request.POST or None, user=request.user)

    if form.is_valid():
        sale = form.save(commit=False)
        sale.user = request.user
        sale.save()
        return redirect(list_sales)

    return render(request, 'transactions/sale-form.html', {'form': form})

# Desfaz vendas
def delete_sale (request, id):
    
    sale = Sale.objects.get(id=id)

    if request.method == 'POST':
        sale.delete()
        return redirect(list_sales)
        
    return render(request, 'transactions/sale-delete.html', {'sale' : sale})

# Desfaz compras
def delete_purchase (request, id):
    
    purchase = Purchase.objects.get(id=id)

    if request.method == 'POST':
        purchase.delete()
        return redirect(list_purchases)
        
    return render(request, 'transactions/purchase-delete.html', {'purchase' : purchase})