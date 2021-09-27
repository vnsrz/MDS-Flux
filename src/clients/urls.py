from django.urls import path
from .views import list_clients, create_client, update_client, delete_client

urlpatterns = [
    path('clients/', list_clients, name='list_clients'),
    path('new', create_client, name='create_clients'),
    path('update/<int:id>/', update_client, name='update_client'),
    path('delete/<int:id>/', delete_client, name='delete_client'),
]