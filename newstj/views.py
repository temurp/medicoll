# -*- coding: utf-8 -*-
# Tajik version
from .models import Newstj, Imagetj
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

def news_list(request):
	news_list = Newstj.objects.order_by("-creation_date")[:3]
	quotes = {'Эмомалӣ Раҳмон': 'Духтур ҳуқуқи маънавии хато кардан надорад, зеро дар дасти ӯ ҳаёти шахс мебошад.',
	'Абӯали ибни Сино': 'Нест беморони ноумед. Танҳо духтурони ноумед хастанд.',
	'Шекспир': 'Саломати аз тилло бештар аст',
	'Андреас Везалий': 'Дар илм сохтори бадани инсон сазовори дониши инсон аст ва сазовори тасдиқи ҳолати фавқулодда.',
	'Конфутсий': 'Манфиатҳои дониши мавҷуда дар татбиқи онҳо.',
	'П.А. Гертсен': '... Дар Ҷарроҳи ҳақ дорад, то ба корд, ба анатомия ва ањвол физиологии имконпазир ва сабабҳои онҳо намедонист, дорад.',
	'Г. Ратнер': 'Физиология - илм, ки метавонад ба шахсе, ки чӣ узвҳои дохилӣ худро баён, дар ҳоле, ки ӯ зиндагӣ мекунад.'}
	author, quote = random.choice(list(quotes.items()))
	return render_to_response('newstj/news_list_tj.html', {'news_list': news_list, 'author': author, 'quote': quote})

def news_detail(request, pk):
	news = Newstj.objects.get(id=pk)
	image = Imagetj.objects.get(news_id=pk)
	news_list = Newstj.objects.order_by("-creation_date")[:5]
	return render_to_response('newstj/news_detail_tj.html', {'news': news,
															'news_list': news_list, 'image': image})

def about_university(request):
	return render_to_response('newstj/about_university_tj.html')

def culture(request):
	return render_to_response('newstj/culture_tj.html')

def enrollee(request):
	return render_to_response('newstj/enrollee_tj.html')

def faculties(request):
	return render_to_response('newstj/faculties_tj.html')

def contacts(request):
	return render_to_response('newstj/contacts_tj.html')

def all_news(request):
	news_list1 = Newstj.objects.all()
	paginator = Paginator(news_list1, 5)
	page = request.GET.get('page')
	try:
		news_list1 = paginator.page(page)
	except PageNotAnInteger:
		news_list1 = paginator.page(1)
	except EmptyPage:
		news_list1 = paginator.page(paginator.num_pages)

	return render_to_response('newstj/news_and_events_tj.html', {'all_news': news_list1})
