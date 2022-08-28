from PIL import Image
from pictures.models import Picture
from pictures.utils import thumbnail
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

def picture_response(request, id):
	pic = Picture.objects.get(id=id)
	img = Image.open(pic.image)
	img_format = img.format

	size = None

	if request.GET.has_key('w') or request.GET.has_key('h'):
		w = request.GET.get('w', img.size[0])
		h = request.GET.get('h', img.size[1])
		size = (w, h)

	if size:
		img = thumbnail(img, size)

	mimetype = 'image/%s' % img_format.lower()
	response = HttpResponse(mimetype=mimetype)

	img.save(response, img_format)
	response['Content-Length'] = response.tell()

	return response


def staff_required(view):
	def wrap(request, *args, **kwargs):
		if not request.user.is_staff:
			return HttpResponseForbidden()
		return view(request, *args, **kwargs)
	return wrap



@csrf_exempt
@staff_required
def picture_upload(request):
	# for jwysiwyg editor upload picture
	if request.method == 'POST':
		f = request.FILES['picture']

		pic = Picture(
				author=request.user,
				image=f,
				)
		pic.save()
		return render_to_response('pictures/upload_completed.html', {
			'picture': pic
			}, context_instance=RequestContext(request)) 

	return render_to_response('pictures/upload.html', {
		}, context_instance=RequestContext(request))

@staff_required
def picture_insert(request):	
	return render_to_response('pictures/insert.html', {
		}, context_instance=RequestContext(request))

@staff_required
def picture_insertlist(request):	
	pictures = Picture.objects.order_by('-date_created')
	return render_to_response('pictures/insertlist.html', {
		'pictures': pictures
		}, context_instance=RequestContext(request))


def picture_set(request):
	widget_name = request.REQUEST.get('widget')
	pictures = Picture.objects.order_by('-date_created')

	if request.method == 'POST':
		pass
	else:
		pass

	return render_to_response('pictures/picture_set.html', {
		'pictures': pictures,
		'widget_name': widget_name
		}, context_instance=RequestContext(request))
