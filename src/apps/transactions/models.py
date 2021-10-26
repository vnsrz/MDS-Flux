from django.db import models
from apps.user.models import CustomUser
from apps.clients.models import Client
from django.db.models import Sum
import datetime

class TransactionsManager(models.Manager):
    def get_monthly_income(self):
        today = datetime.date.today()
        return Sale.objects.filter(sale_date__year=today.year, sale_date__month=today.month).aggregate(Sum('price'))['price__sum'] or 0.00

    def get_monthly_expenses(self):
        today = datetime.date.today()
        return Purchase.objects.filter(purchase_date__year=today.year, purchase_date__month=today.month).aggregate(Sum('price'))['price__sum'] or 0.00

class Purchase(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    purchase_date = models.DateField(verbose_name='purchase date', auto_now_add=True)
    
    products = models.TextField(max_length=1000)
    provider = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=20)

    objects = TransactionsManager()

class Sale(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sale_date = models.DateField(verbose_name='sale date', auto_now_add=True)

    products = models.TextField(max_length=1000)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    objects = TransactionsManager()

# class Balance(models.Model):
#     monthly_income = models.DecimalField(decimal_places=2, max_digits=10)
#     monthly_expenses = models.DecimalField(decimal_places=2, max_digits=10)

