# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-02 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watres', '0011_auto_20160816_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='targetusewo',
            name='checkin',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
