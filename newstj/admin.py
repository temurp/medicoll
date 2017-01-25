# Tajik version
from django.contrib import admin
from .models import Newstj, Imagetj, InlineImagetj, PictureAdmintj

admin.site.register(Newstj, PictureAdmintj)
