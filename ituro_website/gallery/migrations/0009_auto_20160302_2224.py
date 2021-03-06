# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_photo_img_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='img',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='img_2',
        ),
        migrations.AddField(
            model_name='photo',
            name='img_select',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Photo'),
        ),
        migrations.AddField(
            model_name='photo',
            name='img_upload',
            field=models.ImageField(blank=True, null=True, upload_to=gallery.models.get_image_upload_path),
        ),
    ]
