# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matte', '0004_auto_20170913_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelabel',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
