# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20170123_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='news_image',
            field=models.ImageField(upload_to='/home/molly/code/medicoll/uploads', verbose_name='Изображение'),
        ),
    ]
