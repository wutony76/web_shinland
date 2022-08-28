from PIL import Image
from profiles.models import Profile
from profiles.forms import ProfileChangeForm, UserChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

@login_required
def profile_change(request):
	profile, created = Profile.objects.get_or_create(user=request.user) 
	if request.method == 'POST':
		profile_form = ProfileChangeForm(request.POST, prefix='profile', instance=profile)
		user_form = UserChangeForm(request.POST, prefix='info', instance=request.user)
		if profile_form.is_valid() and	user_form.is_valid():
			profile_form.save()
			user_form.save()
	else:
		profile_form = ProfileChangeForm(prefix='profile', instance=profile)
		user_form = UserChangeForm(prefix='info', instance=request.user)


	return render_to_response('profiles/profile_change.html', {
		'profile_form': profile_form,
		'user_form': user_form,
		}, context_instance=RequestContext(request))


@login_required
def photo_upload(request):
	if request.method == 'POST':
		profile = request.user.get_profile()
		print request.FILES
		f = request.FILES['photo']
		profile.photo = f
		profile.save()
		return HttpResponseRedirect(reverse('profiles:profile_change'))
		
	return render_to_response('profiles/upload_photo.html', {
		}, context_instance=RequestContext(request))

def userphoto(request, profile_id):
	profile = Profile.objects.get(id=profile_id)
	img = Image.open(profile.photo)
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
