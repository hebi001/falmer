# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_brandingperiod_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='slug',
            field=models.SlugField(default='default', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brandingperiod',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]