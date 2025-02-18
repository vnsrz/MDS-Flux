from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def list_products (request):
    products = Product.objects.all()
    return render (request, 'inventory/products.html', {'products' : products})

def delete_product (request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect(list_products)
        
    return render(request, 'inventory/product-delete.html', {'product' : product})