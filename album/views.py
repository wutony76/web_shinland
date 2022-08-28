from PIL import Image
from album.models import Album, Photo
from album.utils import thumbnail, crop_thumbnail
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

def index(request):
	albums = Album.objects.order_by('-weight', '-date_created')

	return render_to_response('album/index.html', {
		'albums': albums
		}, context_instance=RequestContext(request))

def photo_list(request, album_id):
	album = Album.objects.get(id=album_id)
	photos = album.photo_set.all()

	return render_to_response('album/photolist.html', {
		'album': album,
		'photos': photos
		}, context_instance=RequestContext(request))


#thumb using crop
def photo_thumb(request, photo_id):
	photo = Photo.objects.get(id=photo_id)
	img = Image.open(photo.image)
	img = crop_thumbnail(img, (150, 110))
	response = HttpResponse(mimetype='image/jpeg')
	img.save(response, 'JPEG')
	response['Content-Length'] = response.tell()

	return response

def photo_response(request, photo_id, size=None):
	photo = Photo.objects.get(id=photo_id)
	img = Image.open(photo.image)

	if request.GET.has_key('w') or request.GET.has_key('h'):
		w = request.GET.get('w', img.size[0])
		h = request.GET.get('h', img.size[1])
		size = (w, h)

	if size:
		img = thumbnail(img, size)
	#mimetype = 'image/%s' % img.format
	#filesize = casephoto.image.size
	response = HttpResponse(mimetype='image/jpeg')

	img.save(response, img.format)
	#print dir(img)

	response['Content-Length'] = response.tell()

	return response


def admin_required(view):
	def wrap(request, *args, **kwargs):
		if not request.user.has_perm('album.can_change_album'):
			return HttpResponse('Denied!')
		return view(request, *args, **kwargs)
	return wrap

@csrf_exempt
@admin_required
def photo_upload(request, album_id):
	album = Album.objects.get(id=album_id)
	if request.method == 'POST':
		f = request.FILES['photo']
		photo = Photo(
				author=request.user,
				album=album,
				)
		photo.save()
		print f
		photo.image = f
		photo.save()

	return render_to_response('album/upload.html', {
		'album': album
		}, context_instance=RequestContext(request))


@admin_required
def photo_changelist(request, album_id):
	album = Album.objects.get(id=album_id)
	photo_list = album.photo_set.all()

	return render_to_response('album/photo_changelist.html', {
		'album': album,
		'object_list': photo_list
		}, context_instance=RequestContext(request))  


@csrf_exempt
@admin_required
def cover_reset(request, photo_id):
	print 'cover_reset', cover_reset
	photo = Photo.objects.get(id=photo_id)
	photo.album.cover = photo
	photo.album.save()
	return HttpResponse('')
