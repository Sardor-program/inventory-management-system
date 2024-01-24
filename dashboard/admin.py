from django.contrib import admin
from .models import Category, Product, Order
from django.contrib.auth.models import Group

admin.site.site_header = "SuperMarket Inventory Dashboard"

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    list_filter = ['category']
    search_fields = ['name', 'category']



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
#admin.site.unregister(Group)

