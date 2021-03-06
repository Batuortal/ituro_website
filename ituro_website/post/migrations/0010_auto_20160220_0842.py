# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20160213_0629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsentry',
            old_name='slug',
            new_name='new_slug',
        ),
        migrations.AddField(
            model_name='newsentry',
            name='old_slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
