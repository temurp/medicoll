# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 04:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagetj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_image', models.ImageField(upload_to='images/', verbose_name='Сурат')),
            ],
        ),
        migrations.CreateModel(
            name='Newstj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Сарлавҳа')),
                ('text', models.TextField(verbose_name='Матн')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Санаи сохташудан')),
            ],
            options={
                'verbose_name_plural': 'Ахборхо',
                'verbose_name': 'Ахбор',
                'ordering': ['-creation_date'],
            },
        ),
        migrations.AddField(
            model_name='imagetj',
            name='news_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newstj.Newstj'),
        ),
    ]