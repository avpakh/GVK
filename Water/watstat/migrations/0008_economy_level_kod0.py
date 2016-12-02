# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watstat', '0007_economy_level_checkin'),
    ]

    operations = [
        migrations.AddField(
            model_name='economy_level',
            name='kod0',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
