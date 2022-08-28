from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from models import Contactus
from forms import ContactusForm

def index(request):
	if request.method == 'POST':
		form = ContactusForm(request.POST)
		if form.is_valid():
			body = form.cleaned_data.get('body')
			mail = form.cleaned_data.get('email')
			Contactus.objects.create(body = body, mail = mail)
			return redirect('/')
	else:
		form = ContactusForm()
		print dir(form)
	return render_to_response('contactus/index.html', {
		'form':form,
		}, context_instance=RequestContext(request))
