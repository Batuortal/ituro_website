# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20160302_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=gallery.models.get_thumbnail_upload_path),
        ),
    ]
