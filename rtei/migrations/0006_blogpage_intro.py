# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtei', '0005_resource_model_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='intro',
            field=models.TextField(blank=True),
        ),
    ]
