from django.contrib import admin
from .models import News, Image, InlineImage, PictureAdmin, SliderImage


admin.site.register(News, PictureAdmin)
admin.site.register(SliderImage)
