from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'number', 'email', 'cpf', 'address')
    search_fields = ('name', 'user', 'cpf', 'email')
admin.site.register(Client, ClientAdmin)