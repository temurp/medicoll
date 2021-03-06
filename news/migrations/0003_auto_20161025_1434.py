# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 09:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20161007_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-creation_date'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='image',
            name='newss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News'),
        ),
    ]
