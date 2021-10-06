from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def historico(request):
    return render(request, 'historico.html')

def clientes(request):
    return render(request, 'clientes.html')

def inventario(request):
    return render(request, 'inventario.html')