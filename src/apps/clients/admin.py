from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'cpf', 'address')
    search_fields = ('name', 'cpf', 'email')
admin.site.register(Client, ClientAdmin)