# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watres', '0029_auto_20161102_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporttableland',
            name='areandatype',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reporttableland',
            name='obosobtype',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]