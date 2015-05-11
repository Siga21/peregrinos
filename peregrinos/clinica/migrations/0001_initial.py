# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='citas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('observaciones', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=75)),
                ('apellidos', models.CharField(max_length=75)),
                ('telefono', models.PositiveIntegerField(null=True, blank=True)),
                ('telefono2', models.PositiveIntegerField(null=True, blank=True)),
                ('antiguedad', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('fotografia', models.ImageField(upload_to=b'imagenes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='historial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('comentario', models.TextField()),
                ('fotografia', models.ImageField(upload_to=b'imagenes')),
                ('cliente', models.ForeignKey(default=None, blank=True, to='clinica.clientes', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='citas',
            name='cliente',
            field=models.ForeignKey(default=None, blank=True, to='clinica.clientes', null=True),
            preserve_default=True,
        ),
    ]
