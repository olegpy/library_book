from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=25, blank=True)
    def __unicode__(self):
        return self.name


class Book(models.Model):
    author_post = models.ForeignKey('auth.User')

    name = models.CharField(max_length=25, blank=True)
    author = models.CharField(max_length=25, blank=True)
    public_date = models.DateTimeField(default=timezone.now)
    image = models.FileField(upload_to='static/img/uploads/%Y/%m/%d/')
    description = models.TextField(blank=True)
    genresbooks = models.ManyToManyField('Genre')
    is_no_draft = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
