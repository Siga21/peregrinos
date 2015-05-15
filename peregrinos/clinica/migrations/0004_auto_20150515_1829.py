# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0003_auto_20150513_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='fotografia',
            field=models.ImageField(upload_to=b'imagenes', blank=True),
        ),
    ]
