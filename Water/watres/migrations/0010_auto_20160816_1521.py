# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watres', '0009_table1use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1use',
            name='addition',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='table1use',
            name='land_date',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='table1use',
            name='land_desc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='table1use',
            name='land_naim',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='table1use',
            name='subject',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='table1use',
            name='target_use',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='table1use',
            name='watprot',
            field=models.CharField(blank=True, max_length=800),
        ),
    ]