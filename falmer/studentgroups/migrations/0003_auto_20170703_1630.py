# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentgroups', '0002_auto_20170703_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mslstudentgroup',
            name='logo_url',
            field=models.CharField(default='', max_length=255),
        ),
    ]
