# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0003_frame_segment_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='results_available',
            field=models.BooleanField(default=False),
        ),
    ]
