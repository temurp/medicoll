# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20170123_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='news_image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
