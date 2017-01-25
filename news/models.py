# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from medicoll import settings


class News(models.Model):
	title = models.CharField(u'Заголовок', max_length=200)
	text = models.TextField(u'Текст')
	creation_date = models.DateTimeField(u'Дата создания', auto_now_add=True)

	class Meta:
		verbose_name = u'Новость'
		verbose_name_plural = u'Новости'
		ordering = ['-creation_date']

	def __str__(self):
		return u'{} {}'.format(self.title, self.creation_date)

class Image(models.Model):
	news_id = models.ForeignKey(News)
	news_image = models.ImageField(u'Изображение', upload_to='images/')

class InlineImage(admin.TabularInline):
	model = Image

class PictureAdmin(admin.ModelAdmin):
    inlines = [InlineImage]
