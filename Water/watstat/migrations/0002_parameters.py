# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watstat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id_parameters', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=300, null=True, blank=True)),
                ('value_field', models.CharField(max_length=4, null=True, blank=True)),
            ],
        ),
    ]
