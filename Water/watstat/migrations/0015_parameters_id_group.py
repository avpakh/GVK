# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watstat', '0014_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameters',
            name='id_group',
            field=models.ForeignKey(default=1, to='watstat.Group'),
            preserve_default=False,
        ),
    ]
