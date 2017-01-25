from django.contrib import admin
from .models import News, Image, InlineImage, PictureAdmin


admin.site.register(News, PictureAdmin)
