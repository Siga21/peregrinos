# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
