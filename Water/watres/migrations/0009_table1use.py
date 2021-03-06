# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 15:15
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watres', '0008_auto_20160815_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table1Use',
            fields=[
                ('id_tableuse', models.AutoField(primary_key=True, serialize=False)),
                ('inv_num', models.IntegerField()),
                ('land_naim', models.CharField(max_length=300)),
                ('land_date', models.CharField(max_length=20)),
                ('land_desc', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=500)),
                ('subject_array', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None)),
                ('target_use', models.CharField(max_length=200)),
                ('addition', models.CharField(max_length=800)),
                ('watprot', models.CharField(max_length=800)),
            ],
        ),
    ]
