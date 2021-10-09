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
from apps.products import views as product_views
from apps.clients import views as client_views
from apps.user import views as user_views

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
    path('produtos/', product_views.list_products, name = "produtos"),

    #clientes
    path('clientes/', client_views.list_clients, name = "list_clients"),
    path('clientes/novo', client_views.create_client, name='create_clients'),
    path('clientes/atualizar/<int:id>/', client_views.update_client, name='update_client'),
    path('clientes/deletar/<int:id>/', client_views.delete_client, name='delete_client'),

    #django auth
    path('registrar/', user_views.register, name='register'),
    path('', include("django.contrib.auth.urls")),
]
