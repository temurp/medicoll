# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='news_image',
            field=models.ImageField(upload_to='uploads/', verbose_name='Изображение'),
        ),
    ]
