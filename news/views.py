from models import News, Category
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator

def index(request):
	contacts = News.objects.all()
	return render_to_response('news/index.html',{
		'contacts': contacts,
		}, context_instance=RequestContext(request))

def detail(request, id):
	news = News.objects.get(id=int(id))
	return render_to_response('news/detail.html',{
		'news':news,
		}, context_instance=RequestContext(request))
