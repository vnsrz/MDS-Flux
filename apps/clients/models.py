from django.db import models
from apps.user.models import CustomUser

# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    number = models.CharField(max_length=11)
    email = models.EmailField()
    cpf = models.CharField(max_length=11, unique=False)
    address = models.TextField()
    isActive = models.BooleanField(default=True)
    hasDebt = models.BooleanField(default=False)

    def get_phone(self):
        n = str(self.number)
        return (f'({n[0:2]}) {n[2:7]}-{n[7:]}')
    
    def get_cpf(self):
        n = str(self.cpf)
        return (f'{n[0:3]}.{n[3:6]}.{n[6:9]}-{n[9:]}')

    def get_isActive(self):
        if self.isActive:
            return "Ativo"

    def __str__(self):
        return self.name

    
