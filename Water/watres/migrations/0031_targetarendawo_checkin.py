# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watres', '0030_auto_20161104_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='targetarendawo',
            name='checkin',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
