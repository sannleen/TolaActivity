# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-24 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0030_auto_20180907_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsiteprofile',
            name='city',
            field=models.CharField(blank=True, max_length=85, null=True),
        ),
        migrations.AddField(
            model_name='siteprofile',
            name='city',
            field=models.CharField(blank=True, max_length=85, null=True),
        ),
    ]
