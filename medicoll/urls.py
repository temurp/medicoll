"""medicoll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from news import views

urlpatterns = [
	url(r'^$', views.news_list, name='news_list'),
	url(r'news/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),
    url(r'about/',views.about_university, name='about_university'),
    url(r'culture/',views.culture, name='culture'),
    url(r'applicants/',views.enrollee, name='enrollee'),
    url(r'faculties/',views.faculties, name='faculties'),
    url(r'all-news/',views.all_news, name='news_and_events'),
    url(r'^admin/', admin.site.urls),
]
