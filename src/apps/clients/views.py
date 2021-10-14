from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView

from apps import user
from .models import Client
from .forms import ClientForm

# Create your views here.
def list_clients (request):
    id = request.user.id
    clients= Client.objects.filter(user=id)
    
    return render (request, 'clients/clients.html', {'clients' : clients})

def create_client (request):
    form = ClientForm(request.POST or None)

    if form.is_valid():
        client = form.save(commit=False)
        client.user = request.user
        client.save()
        return redirect(list_clients)

    return render(request, 'clients/clients-form.html', {'form': form})

def update_client (request, id):
    client = Client.objects.get(id=id)
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect(list_clients)

    return render(request, 'clients/clients-form.html', {'form': form, 'client': client}) 

def delete_client (request, id):
    client = Client.objects.get(id=id)

    if request.method == 'POST':
        client.delete()
        return redirect(list_clients)
        
    return render(request, 'clients/client-delete.html', {'client' : client})

def client_profile (request, id):
    client = Client.objects.get(id=id)

    return render(request, 'clients/profile.html', {'client': client}) 