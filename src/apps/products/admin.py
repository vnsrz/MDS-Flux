from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'sell_price', 'buy_price', 'quantity')
    search_fields = ('user', 'name', 'description', 'sell_price', 'buy_price', 'quantity')
admin.site.register(Product, ProductAdmin)