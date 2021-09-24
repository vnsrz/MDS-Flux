from django.db import models
from django.db.models.base import Model

# Create your models here.
class Client(models.Model):
    name = models.TextField()
    number = models.PositiveBigIntegerField()
    email = models.EmailField()
    cpf = models.PositiveBigIntegerField()
    address = models.TextField()