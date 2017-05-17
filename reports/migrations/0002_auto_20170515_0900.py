# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-15 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reports', '0001_initial'),
        ('workflow', '0001_initial'),
        ('indicators', '0002_auto_20170515_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='agreement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.ProjectAgreement'),
        ),
        migrations.AddField(
            model_name='report',
            name='collected',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indicators.CollectedData'),
        ),
        migrations.AddField(
            model_name='report',
            name='complete',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.ProjectComplete'),
        ),
        migrations.AddField(
            model_name='report',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflow.Country'),
        ),
        migrations.AddField(
            model_name='report',
            name='indicator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indicators.Indicator'),
        ),
        migrations.AddField(
            model_name='report',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.WorkflowLevel1'),
        ),
    ]
