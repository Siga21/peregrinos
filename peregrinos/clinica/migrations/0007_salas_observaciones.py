# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0006_auto_20150801_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='salas',
            name='observaciones',
            field=models.TextField(default=None, null=True),
        ),
    ]
