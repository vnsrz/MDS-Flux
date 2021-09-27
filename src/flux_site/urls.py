"""flux_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from produtos.views import list_products
from clients.views import list_clients, create_client, update_client, delete_client
from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path, include

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #index
    path('', views.index, name = "index"),
    path('index', views.index, name = "index"),

    #historico
    path('historico', views.historico, name = "historico"),

    #produtos
    path('produtos/', list_products, name = "produtos"),

    #clientes
    path('clientes/', list_clients, name = "clientes"),
    path('clientes/new', create_client, name='create_clients'),
    path('clientes/update/<int:id>/', update_client, name='update_client'),
    path('clientes/delete/<int:id>/', delete_client, name='delete_client'),

    
    #django auth
    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name ='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name ='logout'),
]
