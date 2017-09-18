# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0041_auto_20170915_0547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='milestone_date',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='country',
            field=models.ManyToManyField(blank=True, null=True, to='workflow.Country'),
        ),
    ]
