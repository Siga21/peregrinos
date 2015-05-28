# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0004_auto_20150515_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='fotografia',
            field=models.ImageField(upload_to=b'imagenes', blank=True),
        ),
    ]
