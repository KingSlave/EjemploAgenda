# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-01 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idPersona', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
    ]
