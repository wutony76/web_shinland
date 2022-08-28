from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def list_filter_toggle(request):
	toggle =  not request.session.get('_show_list_filter', False)
	request.session['_show_list_filter'] = toggle

	print 'toggle', toggle
	return HttpResponse('')

