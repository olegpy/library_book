# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date_publication',
        ),
        migrations.RemoveField(
            model_name='book',
            name='is_draft',
        ),
        migrations.AddField(
            model_name='book',
            name='is_no_draft',
            field=models.BooleanField(default=True),
        ),
    ]
