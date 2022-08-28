from news.models import News, Media as NewsMedia
from guestbook.models import Post
from album.models import Album
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	return render_to_response('index.html', {
		}, context_instance=RequestContext(request))

def home(request):
	album_list = Album.objects.order_by('-weight', '-date_created')[:4]
	newsmedias = NewsMedia.objects.order_by('-news__is_top', '-news__pub_date')[:5]

	return render_to_response('home.html', {
		'newsmedias': newsmedias,
		'album_list': album_list
		}, context_instance=RequestContext(request))


def calendar_view(request):

	posts = Post.objects.order_by('-pub_date')[:3]
	return render_to_response('calendar.html', {
		'posts': posts
		}, context_instance=RequestContext(request))
