# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watres', '0025_auto_20161102_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='table2obosob',
            name='num_r',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
