from django.db import models

from django_test.models.manager import CustomManager


class Category(models.Model):
    name = models.CharField('Категория товара', max_length=64)


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория')
    name = models.CharField('Наименование товара', max_length=128)
    price = models.DecimalField('Цена единицы, руб.', max_digits=10, decimal_places=2)


class Item(models.Model):
    name = models.CharField('Item', max_length=100)
    active = models.BooleanField('Active', default=True)
    objects = CustomManager()


class Person(models.Model):
    name = models.CharField('Item', max_length=100)
    birthday = models.DateField(null=True, blank=False)
