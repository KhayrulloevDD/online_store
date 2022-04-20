from rest_framework import serializers
from .models import Product, OrderItem, Order


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'cost', 'price', 'count')


class OrderItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity')


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'reference_code', 'items', 'order_date')
