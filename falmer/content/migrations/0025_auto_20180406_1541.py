# Generated by Django 2.0.2 on 2018-04-06 14:41

from django.db import migrations
import falmer.content.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0024_auto_20180312_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectioncontentpage',
            name='body',
            field=wagtail.core.fields.StreamField((('section', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock(required=True)), ('heading_image', falmer.content.blocks.FalmerImageChooserBlock(required=False)), ('body', wagtail.core.blocks.StreamBlock((('paragraph', falmer.content.blocks.RichTextWithExpandedContent()),)))))),)),
        ),
    ]