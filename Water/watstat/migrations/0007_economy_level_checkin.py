# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watstat', '0006_basin_level_economy_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='economy_level',
            name='checkin',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
