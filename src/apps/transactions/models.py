from django.db import models
from apps.user.models import CustomUser
from apps.clients.models import Client

class Purchase(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    purchase_date = models.DateField(verbose_name='purchase date', auto_now_add=True)
    
    products = models.TextField(max_length=1000)
    provider = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=20)

class Sale(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sale_date = models.DateField(verbose_name='sale date', auto_now_add=True)

    products = models.TextField(max_length=1000)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)