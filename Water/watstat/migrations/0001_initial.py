# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id_parameters', models.AutoField(serialize=False, primary_key=True)),
                ('categories', models.CharField(max_length=300, null=True, blank=True)),
            ],
        ),
    ]
