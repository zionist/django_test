# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Категория товара', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Наименование товара', max_length=128)),
                ('price', models.DecimalField(verbose_name='Цена единицы, руб.', max_digits=10, decimal_places=2)),
                ('category', models.ForeignKey(verbose_name='Категория', to='models.Category')),
            ],
        ),
    ]
