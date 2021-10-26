from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description')
    search_fields = ('user', 'name', 'description')
admin.site.register(Product, ProductAdmin)