from django.contrib import admin
from .models import Purchase, Sale

# Register your models here.
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'provider', 'products', 'price')
    search_fields = ('user', 'products', 'provider', 'price')
admin.site.register(Purchase, PurchaseAdmin)

class SaleAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'products', 'price')
    search_fields = ('user', 'products', 'client', 'price')
admin.site.register(Sale, SaleAdmin)