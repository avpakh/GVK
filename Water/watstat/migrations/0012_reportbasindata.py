# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watstat', '0011_datareport'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportBasinData',
            fields=[
                ('id_datareport', models.AutoField(primary_key=True, serialize=False)),
                ('god', models.IntegerField(blank=True, null=True)),
                ('kod', models.CharField(blank=True, max_length=200, null=True)),
                ('nai', models.CharField(blank=True, max_length=500, null=True)),
                ('x1', models.FloatField(blank=True, null=True)),
                ('x2', models.FloatField(blank=True, null=True)),
                ('x3', models.FloatField(blank=True, null=True)),
                ('x4', models.FloatField(blank=True, null=True)),
                ('x5', models.FloatField(blank=True, null=True)),
                ('x6', models.FloatField(blank=True, null=True)),
                ('x7', models.FloatField(blank=True, null=True)),
                ('x8', models.FloatField(blank=True, null=True)),
                ('x9', models.FloatField(blank=True, null=True)),
                ('x10', models.FloatField(blank=True, null=True)),
                ('x11', models.FloatField(blank=True, null=True)),
                ('x12', models.FloatField(blank=True, null=True)),
                ('x13', models.FloatField(blank=True, null=True)),
                ('x14', models.FloatField(blank=True, null=True)),
                ('x15', models.FloatField(blank=True, null=True)),
                ('x16', models.FloatField(blank=True, null=True)),
                ('x17', models.FloatField(blank=True, null=True)),
                ('x18', models.FloatField(blank=True, null=True)),
                ('x19', models.FloatField(blank=True, null=True)),
                ('x20', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]