# -*- coding: utf-8 -*-

from .models import News, Image, SliderImage
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

def news_list(request):
	news_list = News.objects.order_by("-creation_date")[:3]
	img = SliderImage.objects.order_by("-date_of_adding")[:3]
	img1, img2, img3 = img
	# slider_num = ['slide-1','slide-2','slide-3']
	# image_with_num = zip	(slider_num,img)
	quotes = {'Эмомали Рахмон': 'Врач не имеет морального права ошибаться, поскольку в его руках судьба человека.',
	'Абу Али ибн Сино': 'Нет безнадежных больных. Есть только безнадежные врачи.',
	'Шекспир': 'Здоровье — дороже золота.',
	'Андреас Везалий': 'Наука о строении человеческого тела является самой достойной для человека областью знаний и заслуживает чрезвычайного одобрения.',
	'Конфуций': 'Польза от имеющихся знаний в их применении.',
	'П.А. Герцен': '...хирург не имеет права браться за нож, не зная анатомии, возможных физиологических осложнений и их причин.',
	'Г. Ратнер': 'Физиология - наука, способная объяснить человеку, чем занимаются его внутренние органы, пока он живет.'}
	author, quote = random.choice(list(quotes.items()))
	return render_to_response('news/news_list.html', {'news_list': news_list, 'author': author, 'quote': quote,
	'img1': img1, 'img2': img2, 'img3': img3})

def news_detail(request, pk):
	news = News.objects.get(id=pk)
	image = Image.objects.get(news_id=pk)
	news_list = News.objects.order_by("-creation_date")[:5]
	return render_to_response('news/news_detail.html', {'news': news,
															'news_list': news_list, 'image': image})

def about_university(request):
	return render_to_response('news/about_university.html')

def culture(request):
	return render_to_response('news/culture.html')

def enrollee(request):
	return render_to_response('news/enrollee.html')

def faculties(request):
	return render_to_response('news/faculties.html')

def contacts(request):
	return render_to_response('news/contacts.html')

def all_news(request):
	news_list1 = News.objects.all()
	paginator = Paginator(news_list1, 5)
	page = request.GET.get('page')
	try:
		news_list1 = paginator.page(page)
	except PageNotAnInteger:
		news_list1 = paginator.page(1)
	except EmptyPage:
		news_list1 = paginator.page(paginator.num_pages)

	return render_to_response('news/news_and_events.html', {'all_news': news_list1})
