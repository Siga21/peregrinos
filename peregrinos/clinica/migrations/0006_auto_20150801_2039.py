# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0005_auto_20150528_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='salas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sala', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='citas',
            name='sala',
            field=models.ForeignKey(default=None, blank=True, to='clinica.salas', null=True),
        ),
    ]
