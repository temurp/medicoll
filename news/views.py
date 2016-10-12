# -*- coding: utf-8 -*-
from .models import News
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def news_list(request):

	news_list = News.objects.all()
	paginator = Paginator(news_list, 3)

	page = request.GET.get('page')
	try:
		news_list = paginator.page(page)
	except PageNotAnInteger:
		news_list = paginator.page(1)
	except EmptyPage:
		news_list = paginator.page(paginator.num_pages)

	return render_to_response('news/news_list.html', {'news_list': news_list})

def news_detail(request, pk):
	news = News.objects.get(id=pk)
	return render_to_response('news/news_detail.html', {'news': news})