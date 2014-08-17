import datetime

from django.db import models
from django.contrib.auth.models import User

class TimedMixin(models.Model):
    class Meta:
        abstract = True

    updated_when = models.DateTimeField(editable=False)
    created_when = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        self.created_when = datetime.datetime.utcnow()
        self.updated_when = datetime.datetime.utcnow()
        super(TimedMixin, self).save(*args, **kwargs)


class Category(TimedMixin):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=999)


class Page(TimedMixin):

    title = models.CharField(max_length=999)
    description = models.CharField(max_length=999)
    slug = models.CharField(max_length=999)

    content = models.TextField()
    # author = models.ForeignKey(User, null=True, blank=True)

    def get_absolute_url(self):
        return u"/pages/%s/" % self.slug if self.slug else "/pages/"

    def render_permalink(self):
        return u"<a href='{url}' title='{title}'>{title}</a>".format(
            title=self.title,
            url=self.get_absolute_url())

    def render_nav_item(self):
        return u"<a href='{url}' class='nav-item-title' title='{title}'>{title}</a>".format(
            title=self.title,
            url=self.get_absolute_url())

    def __str__(self):
        return "Page: %s, at %s" % (self.title, self.slug)

class Dropdown(TimedMixin):
    title = models.CharField(max_length=999)
    pages = models.ManyToManyField(Page)
    top_page = models.ForeignKey(Page, null=True, blank=True, related_name="+")

    def __str__(self):
        return "Dropdown [%s]: %s (%s items)" % (self.id, self.title, self.pages.count())

class Toolbar(TimedMixin):
    dropdowns = models.ManyToManyField(Dropdown)

    def __str__(self):
        return "Toolbar [%s]: (%s items)" % (self.id, self.dropdowns.count())
