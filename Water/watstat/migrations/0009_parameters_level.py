# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watstat', '0008_economy_level_kod0'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameters',
            name='level',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
