# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watres', '0026_table2obosob_num_r'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table2obosob',
            name='area',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='table2obosob',
            name='w_len',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]