# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watstat', '0013_reportbasindatanew'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id_group', models.AutoField(serialize=False, primary_key=True)),
                ('group_name', models.CharField(max_length=300, null=True, blank=True)),
            ],
        ),
    ]
