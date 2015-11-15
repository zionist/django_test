from django.db import models


class Category(models.Model):
    name = models.CharField('Категория товара', max_length=64)


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория')
    name = models.CharField('Наименование товара', max_length=128)
    price = models.DecimalField('Цена единицы, руб.', max_digits=10, decimal_places=2)
