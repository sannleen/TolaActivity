# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 08:07
from __future__ import unicode_literals

# import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
from django_mysql.models import JSONField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('signature', models.BooleanField(default=True)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('beneficiary_name',),
            },
        ),
        migrations.CreateModel(
            name='BinaryField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('data', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('validations', models.CharField(blank=True, max_length=500, null=True)),
                # ('fields', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('fields', JSONField(null=True)),
                ('is_public', models.BooleanField(default=0)),
                ('default_global', models.BooleanField(default=0)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CustomFormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('validations', models.CharField(blank=True, max_length=500, null=True)),
                ('order', models.IntegerField(default=0)),
                ('required', models.BooleanField(default=0)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distribution_name', models.CharField(max_length=255)),
                ('distribution_implementer', models.CharField(blank=True, max_length=255, null=True)),
                ('reporting_period', models.CharField(blank=True, max_length=255, null=True)),
                ('total_beneficiaries_received_input', models.IntegerField(blank=True, null=True)),
                ('distribution_location', models.CharField(blank=True, max_length=255, null=True)),
                ('input_type_distributed', models.CharField(blank=True, max_length=255, null=True)),
                ('distributor_name_and_affiliation', models.CharField(blank=True, max_length=255, null=True)),
                ('distributor_contact_number', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('form_filled_by', models.CharField(blank=True, max_length=255, null=True)),
                ('form_filled_by_position', models.CharField(blank=True, max_length=255, null=True)),
                ('form_filled_by_contact_num', models.CharField(blank=True, max_length=255, null=True)),
                ('form_filled_date', models.CharField(blank=True, max_length=255, null=True)),
                ('form_verified_by', models.CharField(blank=True, max_length=255, null=True)),
                ('form_verified_by_position', models.CharField(blank=True, max_length=255, null=True)),
                ('form_verified_by_contact_num', models.CharField(blank=True, max_length=255, null=True)),
                ('form_verified_date', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('distribution_name',),
            },
        ),
        migrations.CreateModel(
            name='FieldType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TrainingAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_name', models.CharField(max_length=255)),
                ('implementer', models.CharField(blank=True, max_length=255, null=True)),
                ('reporting_period', models.CharField(blank=True, max_length=255, null=True)),
                ('total_participants', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('community', models.CharField(blank=True, max_length=255, null=True)),
                ('training_duration', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.CharField(blank=True, max_length=255, null=True)),
                ('end_date', models.CharField(blank=True, max_length=255, null=True)),
                ('trainer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('trainer_contact_num', models.CharField(blank=True, max_length=255, null=True)),
                ('form_filled_by', models.CharField(blank=True, max_length=255, null=True)),
                ('form_filled_by_contact_num', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('training_name',),
            },
        ),
    ]
