from django import http

from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.template.loader import render_to_string
from django.shortcuts import render_to_response, get_object_or_404

from getright.models import Page

try:
	admin.site.register(Page)
except:
	pass

admin.autodiscover()

def index(request):
	try:
		page = Page.objects.all()[0]
	except:
		page = Page.objects.create(
			title="Test Page",
			description="This is a test description",
			content="This is a test post content. This is also <em>bold</em>.",
			slug='welcome'
		)

	return render_to_response("base.html", {'page': page})

def get_by_slug(request, page_slug):
	page = get_object_or_404(Page, slug=page_slug)
	return render_to_response("base.html", {'page': page})

urlpatterns = patterns('',
					   # Examples:
					   url(r'^$', index, name='home'),
					   url(r'^pages/(?P<page_slug>\w+)/$', get_by_slug),
					   # url(r'^blog/', include('blog.urls')),

					   url(r'^admin/', include(admin.site.urls)),
					   )
