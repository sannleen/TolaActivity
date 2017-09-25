# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-25 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0056_auto_20170923_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='tolasites',
            name='front_end_url',
            field=models.CharField(default='https://activity.toladata.io', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tolasites',
            name='tola_report_url',
            field=models.CharField(default='https://report.toladata.io', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tolasites',
            name='tola_tables_url',
            field=models.CharField(default='https://activity.toladata.io', max_length=255, null=True),
        ),
    ]
