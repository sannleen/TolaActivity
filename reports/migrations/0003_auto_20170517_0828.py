# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-17 15:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20170515_0900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='program',
            new_name='workflowlevel1',
        ),
    ]
