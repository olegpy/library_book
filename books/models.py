from django.db import models
# from django.utils import timezone
# from datetime import datetime


class Genre(models.Model):
    name = models.CharField(max_length=25, blank=True)
    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=25, blank=True)
    author = models.CharField(max_length=25, blank=True)
    image = models.FileField(upload_to='static/img/uploads/%Y/%m/%d/')
    description = models.TextField(blank=True)
    # date_publication = models.DateTimeField(default=datetime.now, blank=True)
    # date_publication = models.DateField(default=datetime.date.today)
    genresbooks = models.ManyToManyField('Genre')
    is_draft = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
