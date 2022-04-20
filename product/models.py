from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField('Название', max_length=256, unique=True)
    cost = models.FloatField('Себестоимость товара', default=0, validators=[MinValueValidator(0.0)])
    price = models.FloatField('Цена', default=0, validators=[MinValueValidator(0.0)])
    count = models.PositiveIntegerField('Количество', default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='Продукт')
    quantity = models.PositiveIntegerField('Количество', default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.product.name


class Order(models.Model):

    reference_code = models.CharField('Код', max_length=20)
    items = models.ManyToManyField(OrderItem, verbose_name='Товары')
    order_date = models.DateTimeField('Дата', auto_now=True)

    def __str__(self):
        return self.reference_code
