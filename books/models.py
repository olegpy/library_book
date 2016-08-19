from django.db import models
# from django.utils import timezone
import time
from datetime import date
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=25, blank=True)
    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=25, blank=True)
    author = models.CharField(max_length=25, blank=True)
    image = models.FileField(upload_to='static/img/uploads/%Y/%m/%d/')
    description = models.TextField(blank=True)
    genresbooks = models.ManyToManyField('Genre')
    is_no_draft = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name