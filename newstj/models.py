# -*- coding: utf-8 -*-
# Tajik version
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from medicoll import settings


class Newstj(models.Model):
	title = models.CharField(u'Сарлавҳа', max_length=200)
	text = models.TextField(u'Матн')
	creation_date = models.DateTimeField(u'Санаи сохташудан', auto_now_add=True)

	class Meta:
		verbose_name = u'Ахбор'
		verbose_name_plural = u'Ахборхо'
		ordering = ['-creation_date']

	def __str__(self):
		return u'{} {}'.format(self.title, self.creation_date)

class Imagetj(models.Model):
	news_id = models.ForeignKey(Newstj)
	news_image = models.ImageField(u'Сурат', upload_to='images/')

class InlineImagetj(admin.TabularInline):
	model = Imagetj

class PictureAdmintj(admin.ModelAdmin):
    inlines = [InlineImagetj]

class SliderImagetj(models.Model):
	slider_image = models.ImageField(u'Тасвир', upload_to='slider-images/')
	date_of_adding = models.DateTimeField(u'Санаи дохилкар', auto_now_add=True)

	class Meta:
		verbose_name = u'Тасвир дар слайдер'
		verbose_name_plural = u'Тасвирҳо дар слайдер'
		ordering = ['-date_of_adding']

	def __str__(self):
		return u'{} {}'.format(self.slider_image.name, self.date_of_adding)
