# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-25 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0022_organization_allow_budget_decimal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='country',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='workflowlevel1',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='stakeholder',
            name='contact',
        ),
        migrations.AlterField(
            model_name='historicalworkflowlevel2',
            name='level2_uuid',
            field=models.CharField(blank=True, db_index=True, default=uuid.uuid4, editable=False, help_text='Unique ID', max_length=255, verbose_name='WorkflowLevel2 UUID'),
        ),
        migrations.AlterField(
            model_name='historicalworkflowlevel2',
            name='progress',
            field=models.CharField(blank=True, choices=[('open', 'Open'), ('awaitingapproval', 'Awaiting Approval'), ('tracking', 'Tracking'), ('inprogress', 'In Progress'), ('invoiced', 'Invoiced'), ('closed', 'Closed')], default='open', max_length=50),
        ),
        migrations.AlterField(
            model_name='workflowlevel1',
            name='level1_uuid',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=255, unique=True, verbose_name='WorkflowLevel1 UUID'),
        ),
        migrations.AlterField(
            model_name='workflowlevel2',
            name='level2_uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, help_text='Unique ID', max_length=255, unique=True, verbose_name='WorkflowLevel2 UUID'),
        ),
        migrations.AlterField(
            model_name='workflowlevel2',
            name='progress',
            field=models.CharField(blank=True, choices=[('open', 'Open'), ('awaitingapproval', 'Awaiting Approval'), ('tracking', 'Tracking'), ('inprogress', 'In Progress'), ('invoiced', 'Invoiced'), ('closed', 'Closed')], default='open', max_length=50),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]