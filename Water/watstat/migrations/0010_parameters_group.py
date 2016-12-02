# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watstat', '0009_parameters_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameters',
            name='group',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
