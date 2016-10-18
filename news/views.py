# -*- coding: utf-8 -*-
from .models import News
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def news_list(request):

	news_list = News.objects.all()
	paginator = Paginator(news_list, 3)

	query = request.GET.get('query')
	if query:
		news_list = news_list.filter(text__icontains=query)
		return render_to_response('news/news_list.html', {'news_list': news_list,
															'query': query})

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
	news_list = News.objects.order_by("-creation_date")[:5]
	return render_to_response('news/news_detail.html', {'news': news,
															'news_list': news_list})

def about_university(request):
	return render_to_response('news/about_university.html')

def culture(request):
	return render_to_response('news/culture.html')

def enrollee(request):
	return render_to_response('news/enrollee.html')