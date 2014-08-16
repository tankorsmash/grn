from django import http

from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

def return_poop(request):
	import requests
	import random
	subreddit = random.choice(['gentlemanboners', 'aww', 'puppies', 'ladyboners', 'scarlettjohansson', 'katyperry', 'davidtennant'])
	resp = requests.get("http://reddit.com/r/%s/top/.json" % subreddit)
	j = resp.json()
	try:
		img_url = j['data']['children'][0]['data']['url']
	except (KeyError, IndexError):
		img_url = ""
	err_count = 0
	while not img_url.endswith(".jpg") or not img_url.endswith('.png') and err_count < 10:
		subreddit = random.choice(['gentlemanboners', 'aww', 'puppies', 'ladyboners', 'scarlettjohansson', 'katyperry', 'davidtennant'])
		resp = requests.get("http://reddit.com/r/%s/top/.json" % subreddit)
		j = resp.json()
		try:
			img_url = j['data']['children'][0]['data']['url']
		except (KeyError, IndexError):
			img_url = ""
		err_count+=1

	return http.HttpResponse("<img src='%s'> %s" % (img_url, subreddit))
	#return http.HttpResponse("sarah is a whore")

urlpatterns = patterns('',
    # Examples:
    url(r'^$', return_poop, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
