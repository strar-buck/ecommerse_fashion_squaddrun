# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-25 16:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import timedelta.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2048)),
                ('type', models.CharField(choices=[('I', 'Image'), ('T', 'Text'), ('J', 'JSON')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=200)),
                ('reward', models.FloatField(default=0)),
                ('status', models.CharField(choices=[('P', 'Published'), ('W', 'Withdrawn')], max_length=1)),
                ('time_limit_required', models.BooleanField(default=False)),
                ('time_limit', timedelta.fields.TimedeltaField(default=0)),
                ('acceptance_threshold', models.FloatField(default=0.9)),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
