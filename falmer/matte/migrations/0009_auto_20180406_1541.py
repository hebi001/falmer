# Generated by Django 2.0.2 on 2018-04-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matte', '0008_matteimage_internal_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='remoteimage',
            name='internal_source',
            field=models.IntegerField(choices=[(100, 'Default'), (200, 'Student Groups - Logo'), (300, 'Events - Feature'), (400, 'Book Market - Listing')], default=100),
        ),
        migrations.AlterField(
            model_name='matteimage',
            name='internal_source',
            field=models.IntegerField(choices=[(100, 'Default'), (200, 'Student Groups - Logo'), (300, 'Events - Feature'), (400, 'Book Market - Listing')], default=100),
        ),
    ]
