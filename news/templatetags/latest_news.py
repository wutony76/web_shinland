import datetime
import re
from news.models import News
from django.template import Library
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

register = Library()

@register.simple_tag
def latest_news():
	today = datetime.datetime.today()
	newss = News.objects.filter(pub_date__lte=today).order_by('-pub_date')[:8]

	return render_to_string('news/latest.html', {
		'object_list': newss
		})

def get_youtube_vid(url):
	from urlparse import urlparse
	vid = None
	querystring = urlparse(url).query
	r = re.search(r'v=(?P<vid>[^&.]+)', querystring)
	if r:
		vid = r.group('vid')
	return vid

@register.simple_tag
def node_media(media):

	if media.youtube:
		vid = get_youtube_vid(media.youtube)

		return """<iframe width="480" height="360" src="http://www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>""" % vid
			
	return '<img src="%s?w=480&h=360" />' % reverse('pictures:picture', args=[media.picture.id])
