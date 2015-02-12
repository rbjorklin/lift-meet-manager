# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lift_tables', '0003_auto_20150212_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='competition_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='competition',
            old_name='competition_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='competition',
            name='city',
            field=models.CharField(default='N/A', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='country_code',
            field=models.CharField(default='N/A', max_length=30),
            preserve_default=True,
        ),
    ]
