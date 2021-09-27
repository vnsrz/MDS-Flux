from django.db import models
from django.db.models.base import Model
#from phonenumber_field.models import PhoneNumberField

# Create your models here.
class Client(models.Model):
    name = models.TextField(max_length=100)
    number = models.TextField()
    email = models.EmailField()
    cpf = models.PositiveBigIntegerField()
    address = models.TextField()