from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.list_products, name='list_products')
]