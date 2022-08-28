from account.forms import AuthenticateForm, SignupForm
#from django_openid.models import Association
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def index(request):

	return render_to_response('account/index.html', {
		}, context_instance=RequestContext(request))

def signup(request, form_class=SignupForm):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect(reverse('auth_login'))

	else:
		form = SignupForm()

	return render_to_response('registration/signup.html', {
		'form': form
		}, context_instance=RequestContext(request))


