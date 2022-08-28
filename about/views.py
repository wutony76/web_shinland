from about.models import About, Category
from album.models import Album
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

def index(request):
	about, created = About.objects.get_or_create(slug='feature')
	return render_to_response('about/index.html', {
		'about': about
		}, context_instance=RequestContext(request))

def environ(request):
	about, created = About.objects.get_or_create(slug='environ')
	if created:
		about.title = u'環境介紹'
		about.save()
	album, created = Album.objects.get_or_create(slug='environ')
	if created:
		album.name = u'環境介紹'
		album.save()
	photos = album.photo_set.order_by('-weight', '-date_created')[:9]
	return render_to_response('about/environ.html', {
		'about': about,
		'photos': photos
		}, context_instance=RequestContext(request))

def traffic(request):
	return render_to_response('about/traffic.html', {
		}, context_instance=RequestContext(request))

def course(request):
	category = Category.objects.get(id=1)
	abouts = category.about_set.order_by('-date_created')
	teachers = User.objects.filter(groups__name='teachers')
	return render_to_response('about/course.html', {
		'abouts': abouts,
		'teachers': teachers
		}, context_instance=RequestContext(request))

def page_view(request, about_id):
	about = About.objects.get(id=about_id)

	pic_sets = about.picture_sets.all()
	print pic_sets
	return render_to_response('about/page.html', {
		'about': about,
		'pic_sets': pic_sets,
		}, context_instance=RequestContext(request))

def teacher_list(request):
	teachers = User.objects.filter(groups__id=1)
	return render_to_response('about/teacher_list.html', {
		'teachers': teachers,
		}, context_instance=RequestContext(request))

def teacher_view(request, user_id):
	user = User.objects.get(id=user_id)
	profile = user.get_profile()
	about = profile.about or ''
	about = about.replace('\n', '<br/>')
	return render_to_response('about/teacher.html', {
		'teacher': user,
		'profile': profile,
		'about': about
		}, context_instance=RequestContext(request))
