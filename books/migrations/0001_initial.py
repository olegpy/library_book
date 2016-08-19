# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, blank=True)),
                ('author', models.CharField(max_length=25, blank=True)),
                ('image', models.FileField(upload_to=b'static/img/uploads/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('date_publication', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_draft', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genresbooks',
            field=models.ManyToManyField(to='books.Genre'),
        ),
    ]
