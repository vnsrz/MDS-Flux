from django.db import models
from apps.user.models import CustomUser

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    sell_price = models.DecimalField(decimal_places=2, max_digits=5)
    buy_price = models.DecimalField(decimal_places=2, max_digits=5)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
