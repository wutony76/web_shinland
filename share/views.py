import urllib2
from models import Download, Article, ArticleCategory
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.encoding import force_unicode

def index(request):

	return render_to_response('share/index.html', {
		}, context_instance=RequestContext(request))


def article_index(request):
	categories = [
			(category, Article.objects.filter(category=category).order_by('-weight', '-pub_date')[:6])
			for category in ArticleCategory.objects.order_by('-weight')
			]
	#articles = Article.objects.order_by('-pub_date')

	return render_to_response('share/article_index.html', {
		'categories': categories
		}, context_instance=RequestContext(request))

def download_list(request):
	downloads = Download.objects.order_by('-pub_date')

	return render_to_response('share/download_list.html', {
		'downloads': downloads
		}, context_instance=RequestContext(request))

def download(request, obj_id):
	obj = Download.objects.get(id=obj_id)
	mimetype = obj.mimetype or 'application/x-unknown'
	response = HttpResponse(obj.file.read(), mimetype=mimetype)
	response['Content-Disposition'] = u'attachment; filename="%s.%s"' % (
			urllib2.quote(obj.title.encode('utf8')),
			obj.ext)
	#respnse['Content-Length'] = obj.file
	return response

