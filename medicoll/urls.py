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
from django.conf.urls.static import static
from django.contrib import admin

from news import views
from newstj import views as viewstj
from medicoll import settings

urlpatterns = [
	url(r'^$', viewstj.news_list, name='news_list'),
    url(r'^ru/$', views.news_list, name='news_list_ru'),
	url(r'news/(?P<pk>\d+)/$', viewstj.news_detail, name='news_detail'),
    url(r'ru/news/(?P<pk>\d+)/$', views.news_detail, name='news_detail_ru'),
    url(r'about/',viewstj.about_university, name='about_university'),
    url(r'ru/about/',views.about_university, name='about_university_ru'),
    url(r'culture/',viewstj.culture, name='culture'),
    url(r'ru/culture/',views.culture, name='culture_ru'),
    url(r'applicants/',viewstj.enrollee, name='enrollee'),
    url(r'ru/applicants/',views.enrollee, name='enrollee_ru'),
    url(r'faculties/',viewstj.faculties, name='faculties'),
    url(r'ru/faculties/',views.faculties, name='faculties_ru'),
    url(r'all-news/',viewstj.all_news, name='news_and_events'),
    url(r'ru/all-news/',views.all_news, name='news_and_events_ru'),
    url(r'contacts/',viewstj.contacts, name='contacts'),
    url(r'ru/contacts/',views.contacts, name='contacts_ru'),
    url(r'^admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
