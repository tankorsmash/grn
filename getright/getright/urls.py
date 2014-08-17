from django import http

from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.template.loader import render_to_string
from django.shortcuts import render_to_response, get_object_or_404

from getright.models import Page, Dropdown, Toolbar

try:
	admin.site.register(Page)
	admin.site.register(Dropdown)
	admin.site.register(Toolbar)
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

	pages = Page.objects.all()
	toolbar = Toolbar.objects.all()[0]
	return render_to_response("base.html", {
		'page': page,
		'pages' : pages,
		'toolbar' : toolbar,
	})

def get_by_slug(request, page_slug):
	page = get_object_or_404(Page, slug=page_slug)
	pages = Page.objects.all()
	toolbar = Toolbar.objects.all()[0]
	return render_to_response("base.html", {
		'page': page,
		'pages' : pages,
		'toolbar' : toolbar,
	})

urlpatterns = patterns('',
					   # Examples:
					   url(r'^$', index, name='home'),
					   url(r'^pages/(?P<page_slug>\w+)/$', get_by_slug),
					   # url(r'^blog/', include('blog.urls')),

					   url(r'^admin/', include(admin.site.urls)),
					   )
