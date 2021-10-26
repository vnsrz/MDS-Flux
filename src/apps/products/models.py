from django.db import models
from apps.user.models import CustomUser

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.name
