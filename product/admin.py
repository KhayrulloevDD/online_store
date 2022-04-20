from django.contrib import admin
from .models import Product, Order, OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity']
    ordering = ['id']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'reference_code', 'order_date']
    ordering = ['id']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cost', 'price', 'count']
    ordering = ['id']
