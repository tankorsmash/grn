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
        return "/pages/%s/" % self.slug if self.slug else "/pages/"
