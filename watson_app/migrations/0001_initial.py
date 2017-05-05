# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-05 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tone_json', models.TextField(null=True)),
                ('is_prediction_correct', models.NullBooleanField()),
                ('date', models.DateTimeField(null=True)),
            ],
        ),
    ]
