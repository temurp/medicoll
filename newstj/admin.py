# Tajik version
from django.contrib import admin
from .models import Newstj, Imagetj, InlineImagetj, PictureAdmintj, SliderImagetj

admin.site.register(Newstj, PictureAdmintj)
admin.site.register(SliderImagetj)
