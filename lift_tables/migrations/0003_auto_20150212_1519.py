# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lift_tables', '0002_auto_20150212_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='competition_type',
            field=models.CharField(max_length=13),
            preserve_default=True,
        ),
    ]
