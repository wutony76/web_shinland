from models import Post, Reply
from forms import PostForm, BodyForm
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

def index(request):

	p = int(request.GET.get('p', 1))
	qs = Post.objects.order_by('-pub_date')
	paginator = Paginator(qs, 20)
	contacts = paginator.page(p)

	return render_to_response('guestbook/index.html', {
		'contacts': contacts
		}, context_instance=RequestContext(request))

def post_detail(request, obj_id):
	post = Post.objects.get(id=obj_id)

	return render_to_response('guestbook/detail.html', {
		'post': post
		}, context_instance=RequestContext(request))

def post_add(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			if request.user.is_authenticated():
				obj.user = request.user
			obj.ipaddr = request.META['REMOTE_ADDR']
			obj.save()
		
		return redirect(reverse('gcalendar:index'))

	return HttpResponse()

def post_reply(request, obj_id):
	post = Post.objects.get(id=obj_id)
	if request.method == 'POST':
		form = BodyForm(request.POST)
		if form.is_valid():
			body = form.cleaned_data.get('body')
			reply = Reply(
					post=post,
					author=request.user,
					body=body
					)
			reply.save()

	return redirect(reverse('guestbook:post_detail', args=[obj_id]))


