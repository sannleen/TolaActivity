# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0062_auto_20171005_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workflowteam',
            name='workflowlevel1',
        ),
        migrations.AddField(
            model_name='workflowteam',
            name='workflowlevel1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.WorkflowLevel1'),
        ),
    ]
