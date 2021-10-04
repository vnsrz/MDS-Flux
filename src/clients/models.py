from django.db import models
from django.db.models.base import Model
from django.core.validators import RegexValidator

# Create your models here.
class Client(models.Model):
    name = models.TextField(max_length=100)
    number = models.CharField(max_length=11)
    email = models.EmailField()
    cpf = models.CharField(max_length=11, unique=True)
    address = models.TextField()
    
    def get_phone(self):
        n = str(self.number)
        return (f'({n[0:2]}) {n[2:7]}-{n[7:]}')
