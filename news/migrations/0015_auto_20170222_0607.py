# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20170220_1211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sliderimage',
            options={'ordering': ['-date_of_adding'], 'verbose_name': 'Изображение в слайдере', 'verbose_name_plural': 'Изображения в слайдере'},
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='date_of_adding',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата загрузки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='slider_image',
            field=models.ImageField(upload_to='slider-images/', verbose_name='Изображение'),
        ),
    ]