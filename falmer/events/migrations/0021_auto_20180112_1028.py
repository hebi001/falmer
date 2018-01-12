# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_brandingperiod_event_append'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ticket_type',
            field=models.CharField(choices=[('NA', 'n/a'), ('NT', 'Native'), ('MSL', 'MSL')], default='NA', max_length=3),
        ),
    ]
