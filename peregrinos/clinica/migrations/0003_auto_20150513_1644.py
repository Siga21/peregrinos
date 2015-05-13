# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_auto_20150513_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
