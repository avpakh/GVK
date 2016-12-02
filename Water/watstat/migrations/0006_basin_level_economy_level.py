# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watstat', '0005_adm_level_checkin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basin_level',
            fields=[
                ('i_blevel', models.AutoField(serialize=False, primary_key=True)),
                ('kod1', models.CharField(max_length=20, null=True, blank=True)),
                ('nai', models.CharField(max_length=300, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Economy_level',
            fields=[
                ('i_elevel', models.AutoField(serialize=False, primary_key=True)),
                ('level', models.IntegerField(null=True, blank=True)),
                ('god', models.IntegerField(null=True, blank=True)),
                ('kod1', models.CharField(max_length=200, null=True, blank=True)),
                ('nai', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
    ]
