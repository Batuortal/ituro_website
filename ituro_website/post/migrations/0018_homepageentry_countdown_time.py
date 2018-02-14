# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-02-08 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_commonentry_countdown_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepageentry',
            name='countdown_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]