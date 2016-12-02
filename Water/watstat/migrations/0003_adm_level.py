# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watstat', '0002_parameters'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adm_level',
            fields=[
                ('i_alevel', models.AutoField(serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=20, null=True, blank=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('level', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
